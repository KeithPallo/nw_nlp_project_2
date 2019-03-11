#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import nltk
import re
import string
from collections import Counter
import json

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from parse_url import *
from mapping_urls_make import *


def get_test_ingredients(og_ingredients):
    test_ingredients = [x['name'] for x in og_ingredients]

    return test_ingredients


def clean_text(s):
    # import stop words
    stop_words = set(stopwords.words('english'))

    s = re.sub("[^a-zA-Z ]", ' ', s)
    s = s.lower()
    s = word_tokenize(s)

    # filter out stop words
    words = [w for w in s if not w in stop_words]

    return words


def get_cuisine_ingredients(all_recipes, cuisine_name):
    cuisine_df = pd.read_json(all_recipes)
    my_df = cuisine_df[cuisine_df['cuisine'] == cuisine_name]

    cuisine = []
    #print(cuisine_df['ingredients'].tolist())
    for i in my_df['ingredients'].tolist():
        for j in i:
            #print(j)
            cuisine.append(j)

    return cuisine


def get_ngrams(i_list):
    all_grams = []

    for i in i_list:
        l = clean_text(i)
        grams = list(nltk.everygrams(l, max_len=len(l)))
        grams.sort(key=len, reverse=True)
        grams = [' '.join(g) for g in grams]
        if not grams:
            grams.append(i)
        all_grams.append(grams)

    return all_grams


def get_cuisine_kb(cuisine_ingredients_list, ingredients_kb):
    # create PorterStemmer object for stemming words
    ps = PorterStemmer()

    cuisine_kb = {}

    cuisine_grams = get_ngrams(cuisine_ingredients_list)

    for category in ingredients_kb:
        counter = Counter()
        l = [ps.stem(x) for x in ingredients_kb[category]]
        l += ingredients_kb[category]

        for i in cuisine_grams:
            for j in i:
                if j in l:
                    #print(l[l.index(ps.stem(j))])
                    #print(j)
                    counter[j] += 1
                    break

        if counter:
            cuisine_kb[category] = counter.most_common()

    return cuisine_kb


def transform_ingredients(test_ingredients, cuisine_kb, ingredients_kb):
    # create PorterStemmer object for stemming words
    ps = PorterStemmer()

    transformed_ingredients = []
    og_simplified_ingredients = []
    counter = Counter()

    test_grams = get_ngrams(test_ingredients)

    for i in test_grams:
        match = False

        for g in i:
            for category in ingredients_kb:
                ingredients_stemmed = [ps.stem(x) for x in ingredients_kb[category]]
                cuisine_stemmed = [ps.stem(x[0]) for x in cuisine_kb[category]]

                if ps.stem(g) in ingredients_stemmed:
                    og = g
                    new = g

                    if (len(cuisine_kb[category]) > counter[category]) and ps.stem(g) not in cuisine_stemmed[:2]:
                        new = cuisine_kb[category][counter[category]][0]
                        #og_simplified_ingredients.append(g)
                        #transformed_ingredients.append(cuisine_kb[category][counter[category]][0])
                        counter[category] += 1
                        #break

                    if ps.stem(new) in [ps.stem(x) for x in transformed_ingredients]:
                        if (len(cuisine_kb[category]) > counter[category]):
                            counter[category] += 1
                            new = cuisine_kb[category][counter[category]][0]

                    transformed_ingredients.append(new)
                    og_simplified_ingredients.append(og)
                    match = True
                    break

            if match:
                break

        if not match:
            og_simplified_ingredients.append(i[0])
            transformed_ingredients.append(i[0])

    return transformed_ingredients, og_simplified_ingredients


# takes our created italian ingredients KB and list of all recipes, writes dict of italian ingredients + frequencies divided by food group to json
def get_cuisine_ingredients_dict(cuisine_json, all_recipes, cuisine_name):
    # import cuisine ingredients KB (dict of food categories)
    with open(cuisine_json) as json_file:
        ingredients_kb = json.load(json_file)

    # import all_recipes json, get ingredients from only cuisine recipes
    cuisine_ing = get_cuisine_ingredients(all_recipes, cuisine_name)

    # calculate dict of cuisine ingredients + frequencies (keys=food categories)
    cuisine_kb = get_cuisine_kb(cuisine_ing, ingredients_kb)

    # write dict to json file
    name = 'cuisine_kbs/' + cuisine_name + '_kb.json'
    with open(name, 'w') as f:
        json.dump(cuisine_kb, f)

    return cuisine_kb, cuisine_ing


# takes list of og_ingredients (from main_parse) + italian ingredients json file, ingredients KB json file, and returns list of transformed ingredients + simplified og ingredients
def to_cuisine_ingredients(og_ingredients, cuisine_kb, ingredients_kb):
    # get ingredients from recipe being transformed
    test_ingredients = get_test_ingredients(og_ingredients)

    # gets list of transformed ingredients
    transformed_ingredients, og_simplified_ingredients = transform_ingredients(test_ingredients, cuisine_kb, ingredients_kb)

    return transformed_ingredients, og_simplified_ingredients


#takes lists of simplified og ingredients, og directions, transformed ingredients and returns list of new directions
def to_cuisine_directions(og_simplified_ingredients, og_directions, transformed_ingredients):
    new_directions = '@'.join(og_directions)

#    og_grams = get_ngrams(og_ingredients)
#     for i in og_grams:
#         for j in i:
#             if j in new_directions:
#                 new_directions = new_directions.replace(j, transformed_ingredients[og_grams.index(i)])
#                 break

    for i in og_simplified_ingredients:
        if i in new_directions:
            new_directions = new_directions.replace(i, transformed_ingredients[og_simplified_ingredients.index(i)])

    new_directions = new_directions.split('@')

    return new_directions

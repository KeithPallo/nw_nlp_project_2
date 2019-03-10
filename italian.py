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
    stop_words = set(stopwords.words('english'))
    s = re.sub("[^a-zA-Z ]", ' ', s)
    s = s.lower()
    s = word_tokenize(s)
    
    # filter out stop words
    words = [w for w in s if not w in stop_words]
    
    return words


def get_italian_ingredients(all_recipes):
    cuisine_df = pd.read_json(all_recipes)
    italian_df = cuisine_df[cuisine_df['cuisine'] == 'italian']
    
    italian = []
    #print(italian_df['ingredients'].tolist())
    for i in italian_df['ingredients'].tolist():
        for j in i:
            #print(j)
            italian.append(j)
            
    return italian


def get_ngrams(i_list):
    all_grams = []
    
    for i in i_list:
        l = clean_text(i)
        grams = list(nltk.everygrams(l, max_len=len(l)))
        grams.sort(key=len, reverse=True)        
        grams = [' '.join(g) for g in grams]
        all_grams.append(grams)
    
    return all_grams


def get_italian_kb(italian, ingredients_kb):
    ps = PorterStemmer()
    
    italian_kb = {}
    
    italian_grams = get_ngrams(italian)

    for category in ingredients_kb:
        counter = Counter()
        l = [ps.stem(j) for j in ingredients_kb[category]]
        
        for i in italian_grams:
            for j in i:
                if ps.stem(j) in l:                    
                    counter[j] += 1
                    break
                
        if counter:
            italian_kb[category] = counter.most_common()
            
    return italian_kb


def transform_ingredients(test_ingredients, italian_kb, ingredients_kb):
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
                italian_stemmed = [ps.stem(x[0]) for x in italian_kb[category]]

                if ps.stem(g) in ingredients_stemmed:
                    og = g
                    new = g 
                      
                    if (len(italian_kb[category]) > counter[category]) and ps.stem(g) not in italian_stemmed[:2]:
                        new = italian_kb[category][counter[category]][0]
                        #og_simplified_ingredients.append(g)
                        #transformed_ingredients.append(italian_kb[category][counter[category]][0])
                        counter[category] += 1
                        #break
                        
                    if ps.stem(new) in [ps.stem(x) for x in transformed_ingredients]:
                        if (len(italian_kb[category]) > counter[category]):
                            counter[category] += 1
                            new = italian_kb[category][counter[category]][0]
                    
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
def get_italian_ingredients_dict(italian_json, all_recipes):
    # import stop words
    #stop_words = set(stopwords.words('english'))
    
    # create PorterStemmer object for stemming words
    #ps = PorterStemmer()
    
    # import italian ingredients KB (dict of food categories)
    with open(italian_json) as json_file:
        ingredients_kb = json.load(json_file)
        
    # import all_recipes json, get ingredients from only italian recipes
    italian = get_italian_ingredients(all_recipes)
    
    # calculate dict of italian ingredients + frequencies (keys=food categories)
    italian_kb = get_italian_freq(italian, ingredients_kb)
    
    # write dict to json file
    with open('italian_freq.json', 'w') as f:
        json.dump(italian_kb, f)
        
    return italian_kb


# takes list of og_ingredients (from main_parse) + italian ingredients json file, ingredients KB json file, and returns list of transformed ingredients + simplified og ingredients
def cuisine_to_italian_ingredients(og_ingredients, italian_kb, ingredients_kb):        
    # get ingredients from recipe being transformed
    test_ingredients = get_test_ingredients(og_ingredients)
    
    # gets list of transformed ingredients
    transformed_ingredients, og_simplified_ingredients = transform_ingredients(test_ingredients, italian_kb, ingredients_kb)
    
    return transformed_ingredients, og_simplified_ingredients


#takes lists of simplified og ingredients, og directions, transformed ingredients and returns list of new directions
def cuisine_to_italian_directions(og_simplified_ingredients, og_directions, transformed_ingredients):    
    new_directions = '@'.join(og_directions)
    
    print(og_directions)
    
    for i in og_simplified_ingredients:
        if i in new_directions:
            new_directions = new_directions.replace(i, transformed_ingredients[og_simplified_ingredients.index(i)])

    new_directions = new_directions.split('@')
                           
    return new_directions
# Load in necesarry libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import re
import string
import copy
import collections
from collections import Counter
import ing_parser
from pprint import pprint

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams

from parse_url import *


# Write rules - two sets for healthy / unhealthy

file_rules_to_health = {'alcohol': ('nothing', []),
 'beef': ('replace_then_non', ['low fat turkey']),
 'binders': ('nothing', []),
 'carb': ('replace_then_lowcarb', ['quinoa']),
 'cheeses': ('replace_then_non', []),
 'condiments': ('replace_then_low_sugar', []),
 'dairy': ('replace_then_non', []),
 'dishes': ('nothing', []),
 'drinks': ('nothing', []),
 'fats': ('replace_then_nothing', ['extra virgin olive oil']),
 'fruits': ('nothing', []),
 'other_protein': ('nothing', []),
 'poultry': ('nothing', []),
 'sauces': ('replace_then_non', []),
 'seafood': ('replace_then_nothing', ['wildcaught salmon']),
 'seasoning': ('nothing', []),
 'soups': ('nothing', []),
 'sugars': ('replace_then_nothing', ['stevia', 'spartame', 'saccharin']),
 'veg_nuts': ('nothing', [])}

# First version being testing

file_rules_to_unhealthy = {'alcohol': ('nothing', []),
 'beef': ('replace_then_full_fat', ['80% lean ground beef with 20% fat']),
 'binders': ('nothing', []),
 'cheeses': ('replace_then_full_fat', []),
 'dairy': ('replace_then_full_fat', []),
 'dishes': ('nothing', []),
 'drinks': ('nothing', []),
 'fats': ('replace_then_full_fat', ['heavily salted butter']),
 'fish': ('replace_then_full_fat', ['full fat chicken thighs']),
 'fruits': ('sugar_covered', []),
 'grains': ('replace_then_full_fat', ['heavily buttered biscuits']),
 'nuts': ('nothing', []),
 'oils': ('replace_then_nothing', ['full fat canola oil']),
 'other_protein': ('fried', []),
 'pasta': ('replace_then_nothing', []),
 'poultry': ('replace_then_full_fat', ['full fat chicken thighs']),
 'sauces': ('replace_then_high_sodium', []),
 'seafood': ('replace_then_heavy_butter', []),
 'seasoning': ('replace_then_nothing',[]),
 'soups': ('nothing', []),
 'sugars': ('replace_then_nothing', []),
 'vegetables': ('nothing', [])}



def clean_text(s):
    # Helper function for KB comparison
    tokens = word_tokenize(s)
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]

    # filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    words = [word for word in stripped if word.isalpha()]

    return words


def comp_to_kb(ing_list,ingredientsKB):
    # Function for comparing simple list against KB
    ingredients = {}

    for category in ingredientsKB:
        counter = Counter()
        for ingredient in ing_list:
            tokens = clean_text(ingredient)
            # try all permuations in tokens
            for perm in tokens:
                if perm in ingredientsKB[category]:
                    counter[perm] += 1
        if counter:
            ingredients[category] = counter

    return ingredients



def compare_ingredients(dict_1,dict_2):

    master_counter = []

    # Iterate through all keys in one diciontary
    for category in dict_1:

        # Check to see if key exists
        if category in dict_2.keys():

            #create a copy of the first counter
            cop = copy.deepcopy(dict_1[category])

            # subtract the two counters
            cop.subtract(dict_2[category])

            # print(single)

            # take absolute value of all ingredients
            #for ingredient in cop.keys():
            #    cop[ingredient] = abs(cop[ingredient])

            # add the abs diff counter to the master counter
            master_counter.append([category,cop])

        else:
            # account for case where entire group is not in the section dictionary
            master_counter.append([category,dict_1[category]])

    return master_counter




def ing_swap_funtion(kb,ingredients,rules_dict = "to_health"):

    # assumes ingredients are preprocessed going into this function - may need to change this

    if rules_dict == "to_health":
        rules_dict = file_rules_to_health

    elif rules_dict =="to_unhealthy":
        rules_dict = file_rules_to_unhealthy

    else:
        print("ERROR")

    final = []

    # Iterate through all potential ingredients
    for ingredient in ingredients:

        # initialize empty category
        category = ''

        # find appropriate cateogory in KB
        for key,value in kb.items():
            if ingredient in value:
                category = key
                break

        if category != '':
            #print(" Original Ingredient: " + ingredient)
            #print(" Category: " + category)
            # structured to allow different data structures for different rules

            rule = rules_dict[category]
            direction = rule[0]

            # agnostic functions
            if direction == "nothing":
                # do nothing - keep the ingredient
                final.append(ingredient)


            elif direction == "replace_then_nothing":
                # replace until list is empty - then, do nothing to the ingredient

                if rule[1]:
                    val = rules_dict[category][1].pop(0)
                    final.append(val)
                else:
                    final.append(ingredient)


            elif direction == "replace_then_non":
                # replace until list is empty - then add "non-fat " to the ingredient
                if rule[1]:
                    val = rules_dict[category][1].pop(0)
                    final.append(val)
                else:
                    final.append("non-fat " + ingredient)



            elif direction == "replace_then_lowcarb":
                # replace until list is empty - then add "low-card " to the ingredient
                if rule[1]:
                    val = rules_dict[category][1].pop(0)
                    final.append(val)
                else:
                    final.append("low-carb " + ingredient)


            elif direction == "replace_then_low_sugar":
                # replace until list is empty - then add "low-card " to the ingredient
                if rule[1]:
                    val = rules_dict[category][1].pop(0)
                    final.append(val)
                else:
                    final.append("low sugar " + ingredient)




            # Unhealthy direction -------------------------------------------------
            elif direction == "fried":
                # make the ingtedient fried
                final.append("fried " + ingredient)


            elif direction == "replace_then_full_fat":
                # replace then add - "full fat"
                if rule[1]:
                    val = rules_dict[category][1].pop(0)
                    final.append(val)
                else:
                    final.append("full fat " + ingredient)

            elif direction == "replace_then_heavy_butter":
                if rule[1]:
                    val = rules_dict[category][1].pop(0)
                    final.append(val)
                else:
                    final.append("heavily buttered " + ingredient)


            elif direction == "sugar_covered":
                if rule[1]:
                    val = rules_dict[category][1].pop(0)
                    final.append(val)
                else:
                    final.append("sugar covered " + ingredient)



            elif direction == "full_fat_with_cheese":
                pass

            elif direction == "replace_then_high_sodium":
                if rule[1]:
                    val = rules_dict[category][1].pop(0)
                    final.append(val)
                else:
                    final.append("high sodium " + ingredient)

            elif direction == "add_mixed_sugar":
                if rule[1]:
                    val = rules_dict[category][1].pop(0)
                    final.append(val)
                else:
                    final.append(ingredient + " with mixed in sugar")







            else:
                print("unaccounted for case")

        # if not in there, do something ... currently not doing anything (could store values for reference)
        else:
            # currently doing nothing
            final.append(ingredient)

    return final


def clean_ingredients(ingredients,kb):

    clean_ingredients = []

    # Because we are just cleaning the ingredients, we can change the KB into a simple set (assuming are disjoint sets)

    # instance simple kb
    simple_kb = set()

    # build simple kb
    for category in kb.keys():
        current = tuple(kb[category])
        simple_kb.update(current)


    # iterate through all ingredients
    for ingredient in ingredients:

        # make list of all possible
        all_possible = make_all_possible_ngrams(ingredient)

        # get longest version
        longest = find_longest(all_possible,simple_kb)

        # check to make sure it is not empty - if it is, then use the standard version
        if not longest: longest = "not_changed"

        clean_ingredients.append(longest)



    # return all cleaned spring
    clean_ingredients = [x[0] if type(x) == 'list' else x for x in clean_ingredients]

    return clean_ingredients



def make_all_possible_ngrams(ingredient):
    tokens = clean_text(ingredient)

    all_grams = []

    total_len = len(tokens)

    for index in range(0,total_len+1):
        for index_2 in range(index+1,total_len+1):
            all_grams.append(" ".join(tokens[index:index_2]))

    return all_grams


def find_longest(ingredient_list,simple_kb):

    # only keep ingredients that are in the kb
    ingredient_list = [ ing for ing in ingredient_list if ing in simple_kb]

    if not ingredient_list: return []   # return empty list to avoid further errors

    le = max(len(x.split()) for x in ingredient_list)                  #find out the max number of wors

    max_list = [x for x in ingredient_list if len(x.split()) == le]    #now filter list based on that max length

    # If the max_list is not empty, take the first element (current paradigm can change if we like)

    if max_list:
        max_list = max_list[0]

    return max_list



def health_directions(og_simplified_ingredients, og_directions, transformed_ingredients):


    new_directions = '@'.join(og_directions)

    for i in og_simplified_ingredients:
        if i in new_directions:
            new_directions = new_directions.replace(i, transformed_ingredients[og_simplified_ingredients.index(i)])

    new_directions = new_directions.split('@')

    return new_directions

# import the KB - specifically for healthy ingredients

with open("to_health_ingredients_kb.json", 'r') as infile:
    health_kb = json.load(infile)

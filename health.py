#!/usr/bin/env python
# coding: utf-8

# In[6]:


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

from ingredient_parser import en

from pprint import pprint

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams

from parse_url import *


# In[7]:


# Write rules - two sets for healthy / unhealthy

file_rules = {'alcohol': ('nothing', []),
 'beef': ('replace_then_non', ['low fat turkey']),
 'binders': ('nothing', []),
 'carb': ('replace_then_lowcarb', ['quinoa']),
 'cheeses': ('replace_then_non', []),
 'dishes': ('nothing', []),
 'drinks': ('nothing', []),
 'fats ': ('replace_then_nothing', ['extra virgin olive oil']),
 'fruits': ('nothing', []),
 'other_protein': ('nothing', []),
 'poultry': ('replace_then_nothing', ['wildcaught salmon']),
 'sauces': ('replace_then_non', []),
 'seasoning': ('nothing', []),
 'soups': ('nothing', []),
 'sugars': ('replace_then_nothing', ['stevia', 'spartame', 'saccharin']),
 'veg_nuts': ('nothing', [])}


# In[8]:


# Helper function for KB comparison

def clean_text(s):
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


# In[9]:


# Function for comparing simple list against KB

def comp_to_kb(ing_list,ingredientsKB):
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


# In[10]:


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






# In[42]:


def ing_swap_funtion(kb,ingredients,rules_dict = file_rules):

    # assumes ingredients are preprocessed going into this function - may need to change this

    final = []

    # pprint(rules_dict.keys())

    # Iterate through all potential ingredients
    for ingredient in ingredients:
        #print(ingredient)
        #print(final)
        # initialize empty category
        category = ''

        # find appropriate cateogory in KB
        for key,value in kb.items():
            if ingredient in value:
                category = key
                break

        if category != '':
            # structured to allow different data structures for different rules

            # lookup value in rules_dict

            # print(category)
            #print(rule)
            rule = rules_dict[category]
            direction = rule[0]

            # agnostic functions
            if direction == "nothing":
                # do nothing - keep the ingredient
                final.append(ingredient)


            elif direction == "replace_then_nothing":
                # replace until list is empty - then, do nothing to the ingredient

                # print(rule)

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

            else:
                print("unaccounted for case")

        # if not in there, do something ... currently not doing anything (could store values for reference)
        else:
            # currently doing nothing
            final.append(ingredient)

    return final


# In[12]:


def clean_ingredients(ingredients,kb):

    clean_ingredients = []

    # Because we are just cleaning the ingredients, we can change the KB into a simple set (assuming are disjoint sets)

    # instance simple kb
    simple_kb = set()

    # build simple kb
    for category in kb.keys():
        #print(category)
        current = tuple(kb[category])
        simple_kb.update(current)


    # iterate through all ingredients
    for ingredient in ingredients:

        # make list of all possible
        all_possible = make_all_possible_ngrams(ingredient)

        # get longest version
        longest = find_longest(all_possible,simple_kb)

        # print(longest)

        # check to make sure it is not empty - if it is, then use the standard version
        if not longest: longest = ingredient

        clean_ingredients.append(longest)



    # return all cleaned spring
    clean_ingredients = [x[0] if type(x) == 'list' else x for x in clean_ingredients]


    return clean_ingredients





# In[13]:


def make_all_possible_ngrams(ingredient):
    tokens = clean_text(ingredient)

    all_grams = []

    total_len = len(tokens)

    for index in range(0,total_len+1):
        for index_2 in range(index+1,total_len+1):
            all_grams.append(" ".join(tokens[index:index_2]))

    return all_grams



# In[14]:


def find_longest(ingredient_list,simple_kb):

    # only keep ingredients that are in the kb
    ingredient_list = [ ing for ing in ingredient_list if ing in simple_kb]

    if not ingredient_list: return []   # return empty list to avoid further errors

    le = max(len(x.split()) for x in ingredient_list)                  #find out the max number of wors

    max_list = [x for x in ingredient_list if len(x.split()) == le]    #now filter list based on that max length

    # If the max_list is not empty, take the first element (current paradigm can change if we like)

    if max_list:
        max_list = max_list[0]

    #print(max_list)
    return max_list




# In[15]:


# import the KB - specifically for healthy ingredients

with open("to_health_ingredients_kb.json", 'r') as infile:
    health_kb = json.load(infile)


# In[18]:


# url1 = 'https://www.allrecipes.com/recipe/228293' # Test url - currently not in use


# In[28]:


# ingredients, directions = main_parse(url1,check="single")
# ingredients = [ i['name'] for i in ingredients]


# In[43]:


#cleaned_ingredients = clean_ingredients(ingredients,health_kb)
# new_ingredients = ing_swap_funtion(health_kb,cleaned_ingredients)


# In[ ]:

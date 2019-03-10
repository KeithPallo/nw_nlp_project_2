
# https://www.allrecipes.com/recipe/228293

# load in standard libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import re
import string
import copy
import collections
import os
from collections import Counter
from ingredient_parser import en
from pprint import pprint

# load in nltk for
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from parse_url import *

# load in module functions
import health
import vegetarian

# python3 -c 'import main; main.run_interface()'

# Potential for importing Jupyter notebook - have not tested this out
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from IPython.display import display, HTML
formatter = HtmlFormatter()


def run_interface():

    _continue = True

    # prompt user to input a URL
    print("Please input your url.")
    url = input()


    # parse url using parse_url.py
    og_ingredients, og_directions = main_parse(url,check="single")
    unfiltered_ingredients = get_full_ingredients(url)

    simple_ingredients = [ i['name'] for i in og_ingredients]

    # write original to text file
    # TO DO

    # load in associated KB's - currtently only healthy

    with open("to_health_ingredients_kb.json", 'r') as infile:
        health_kb = json.load(infile)

    with open("veg_kb.json", 'r') as f:
        veg_kb = json.loads(f.read())


    while _continue:
        # while user wants to continue

        print("Here is the parsed recipe: ")
        for ingredient in og_ingredients: print(ingredient)
        print("------------------------------------------------")

        print("Here is the original recipe: ")
        for ingredient in unfiltered_ingredients: print(ingredient)
        print("------------------------------------------------")


        # display rules for selecting transform
        print(" Please select your desired transform. These are the rules we are going to display.")
        print(" Select 1 to make the recipe healthy.")
        print(" Select 2 to make the recepe unhealthy.")
        print(" Select 3 to make the recipe vegetarian.")
        print(" Select 4 to make the recipe non-vegetarian.")

        print(" Select X to quick the program. ")

        # select next action
        next = input()

        # call transform from imported files

        t_ingredients = copy.deepcopy(simple_ingredients)
        t_full_ingredients = copy.deepcopy(og_ingredients)
        t_directions = copy.deepcopy(og_directions)

        if next == '1':

            # create deep copy to ensure that original never get modified


            # select transform based on input
            cleaned_ingredients = health.clean_ingredients(t_ingredients,health_kb)
            new_ingredients = health.ing_swap_funtion(health_kb,cleaned_ingredients)
            # TO DO - write cleaned directions

        if next == "3":
            new_ingredients, new_directions = vegetarian.makeVegetarian(t_full_ingredients,t_directions,veg_kb)

        if next == "4":
            new_ingredients, new_directions = vegetarian.undoVegetarian(t_full_ingredients,t_directions,veg_kb)




        elif next == "x":
            print("quiting the url currently being tested")
            _continue = False
            return


        pprint(new_ingredients)

        # modify ingredients for printing
        # if next not in ["3","4"]:
        new_ingredients = printPretty(og_ingredients,new_ingredients)

        # print new ingredients
        for ingredient in new_ingredients: print(ingredient)


        # print differences using diff_for_display
        # TO DO - Write function


        # differences = findDifferences(unfiltered_ingredients,new_ingredients)
        # for difference in differences: print(difference)
        # TO DO - write transform to txt file for later processing

def test_internal():
    # read in list of URLS
    # call run interface with optional parameter to input parameter
    pass


def findDifferences(old_ingredients, new_ingredients):
    changes_made = []
    new_ing_dict = dict((k,0) for k in new_ingredients)

    for old in old_ingredients:
        if old in new_ingredients:
            new_ing_dict[old] = 1
        else:
            changes_made.append(old + " -> removed")

    for new in new_ingredients:
        if new_ing_dict[new] == 0:
            changes_made.append("added -> " + new)

    return changes_made


def printPretty(old_stuff_dicts, ingredients):

    new_ingredients = []

    for index in range(0,len(old_stuff_dicts)):

        full_new = old_stuff_dicts[index]['quantity'] + ' ' +  old_stuff_dicts[index]['measurement'] + ' ' + ingredients[index]
        new_ingredients.append(full_new)

    return new_ingredients


def display_standard():
    # display ingredients for the user

    pass

def parse_ingredients():
    pass


if __name__ == "__main__":
    # test_interal() - change this to select a specific type of ingredient list
    run_interface()


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
import italian

# python3 -c 'import main; main.run_interface()'

# Potential for importing Jupyter notebook - have not tested this out
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from IPython.display import display, HTML
formatter = HtmlFormatter()


def run_interface(dir="empty",filename="test"):

    _continue = True

    if dir == "empty":

        # prompt user to input a URL
        print("Please input your url.")
        url = input()

    else:
        url = dir
        print(" The url being used is " + url)


    # write url to text file
    file = open('test.txt', "a+")
    file.write('URL being test : ' + dir + '\n\n')
    file.close()


    # parse url using parse_url.py
    og_ingredients, og_directions = main_parse(url,check="single")
    unfiltered_ingredients = get_full_ingredients(url)
    simple_ingredients = [ i['name'] for i in og_ingredients]



    # load in associated KB's - currently only healthy
    with open("to_health_ingredients_kb.json", 'r') as infile:
        health_kb = json.load(infile)

    with open("veg_kb.json", 'r') as f:
        veg_kb = json.loads(f.read())

    with open("to_italian_kb.json", 'r') as i1:
        italian_kb = json.loads(i1.read())

    with open("italian_freq.json", 'r') as i2:
        italian_freq = json.loads(i2.read())


    # Core user interface
    while _continue:

        # while user wants to continue
        print('\n' * 3)
        print("MAIN MENU")
        print("Here is the parsed recipe: ")
        for ingredient in og_ingredients: print(ingredient)
        print("------------------------------------------------")



        print("Here is the original recipe: ")
        for ingredient in unfiltered_ingredients: print(ingredient)
        print("------------------------------------------------")


        # display rules for selecting transform
        print("Please select your desired transform. These are the rules we are going to display.")
        print("Select 1 to make the recipe healthy.")
        print("Select 2 to make the recepe unhealthy.")
        print("Select 3 to make the recipe vegetarian.")
        print("Select 4 to make the recipe non-vegetarian.")
        print("Select 5 to make the recipe Italian.")

        print("Select X to quick the program. ")

        # select next action
        next = input()


        # create deep copy to ensure that original never get modified
        t_ingredients = copy.deepcopy(simple_ingredients)
        t_full_ingredients = copy.deepcopy(og_ingredients)
        t_directions = copy.deepcopy(og_directions)
        t_unfiltered = copy.deepcopy(unfiltered_ingredients)

        # call transform from imported files ------------------------------------------------------------------------


        if next == '1':
            cleaned_ingredients = health.clean_ingredients(t_ingredients,health_kb)
            new_ingredients = health.ing_swap_funtion(health_kb,cleaned_ingredients)
            new_directions = health.health_directions(cleaned_ingredients, t_directions, new_ingredients)

        if next == "2":
            cleaned_ingredients = health.clean_ingredients(t_ingredients,health_kb)
            new_ingredients = health.ing_swap_funtion(health_kb,cleaned_ingredients,rules_dict = "to_unhealthy" )
            new_directions = health.health_directions(cleaned_ingredients, t_directions, new_ingredients)

        if next == "3":
            new_ingredients, new_directions = vegetarian.makeVegetarian(t_full_ingredients,t_directions,veg_kb)

        if next == "4":
            new_ingredients, new_directions = vegetarian.undoVegetarian(t_full_ingredients,t_directions,veg_kb)

        if next == "5":
            new_ingredients, og_simplified_ingredients = italian.cuisine_to_italian_ingredients(og_ingredients, italian_freq, italian_kb)
            new_directions = italian.cuisine_to_italian_directions(og_simplified_ingredients, og_directions, new_ingredients)


        elif next == "x":
            print("quiting the url currently being tested")
            _continue = False
            return

        new_directions = [ s.strip() for s in new_directions]


        # modify ingredients to include measurements, etc.
        if next not in ["3","4"]:
            new_ingredients = printPretty(og_ingredients,new_ingredients,t_unfiltered)
        else:
            pass
            # MARIO - whatever we need to do here

        print("Here is your new recipe! ")
        print("----------------------------------------------------------------------")

        print("The new list of ingredients are:")

        # print new ingredients
        for ingredient in new_ingredients: print(ingredient)


        # show the user the changes in ingredients
        print("----------------------------------------------------------------------")
        print("The changes in the ingredients were: ")

        if next not in ["3","4"]:
            differences = find_swaps(t_unfiltered,new_ingredients)
            for different in differences: print(different)

            # write differences to file for future testing
            file = open('test.txt', "a+")
            for difference in differences:
                file.write('Change : ' + difference + '\n\n')
            file.close()
        else:
            pass


        # print the new directions
        print("----------------------------------------------------------------------")
        print(" The new directions are as follows: ")
        pprint(new_directions)

        # write new directions for testing
        file = open('test.txt', "a+")
        for direction in new_directions:
            file.write('New Direction : ' + direction + '\n\n')
        file.close()

        print( "Press enter to return to the main menu, otherwise enter x to exit")

        check = input()

        if check == "x":
            break

def test_internal():
    # Allows us to test multiple different urls in a row without having to read them in or try multiple

    url_veg = []
    url_nonveg = []
    url_healthy = ['https://www.allrecipes.com/recipe/257865','https://www.allrecipes.com/recipe/23600','https://www.allrecipes.com/recipe/8669','https://www.allrecipes.com/recipe/65896'
                    ]
    url_unhealhy = []
    url_italian = []


    # What do you want to test ?
    print(" What do you want to test?")
    print(" Type: veg, nonveg, healthy, unhealthy, italian?")

    command = input()

    if command == "veg": target = url_veg
    if command == "nonveg": target = url_nonveg
    if command == "healthy": target = url_healthy
    if command == "unhealthy": target = url_unhealthy
    if command == "italian": target = url_italian

    for url in target:
        run_interface(dir=url,filename=("test_" + url))




def find_swaps(old_ingredients,new_ingredients):
    # Find differences between two ingredients lists that are of the same length

    swaps = []

    for index in range(0,len(old_ingredients)):
        if old_ingredients[index] != new_ingredients[index]:
            string = old_ingredients[index] + " - > " + new_ingredients[index]
            swaps.append(string)

    return swaps



def findDifferences(old_ingredients, new_ingredients):
    # Different version of find_swaps - currently not being used.
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


def printPretty(old_stuff_dicts, ingredients,unfiltered):

    new_ingredients = []

    for index in range(0,len(old_stuff_dicts)):


        new_ing = ingredients[index]
        original = unfiltered[index]

        # check if nothing swapped or substring - if not, keep original
        if new_ing == "not_changed" or new_ing in original:
            new_ingredients.append(original)

        # UPDATE TO BETTER IMPLEMENTATION -- use parsing from unfiltered
        else:
            # update with new measurement
            full_new = old_stuff_dicts[index]['measure'] + ' ' + ingredients[index]

            new_ingredients.append(full_new)

    return new_ingredients



if __name__ == "__main__":
    test_internal()
    # run_interface()


# Sample test URL
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
import ing_parser
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
import cuisine


# Potential for importing Jupyter notebook - currently no use
# from pygments import highlight
# from pygments.lexers import PythonLexer
# from pygments.formatters import HtmlFormatter
# from IPython.display import display, HTML
# formatter = HtmlFormatter()


def run_interface(dir="empty",filename="test"):

    _continue = True

    if dir == "empty":

        # prompt user to input a URL
        print("Please input your url.")
        url = input()

    else:
        url = dir
        print("The url being used is " + url)


    # write url to text file
    file = open('test.txt', "a+")
    file.write('URL being test : ' + dir + '\n\n')
    file.close()


    # parse url using parse_url.py
    og_ingredients, og_directions, og_name = main_parse(url,check="single",veg="true")
    unfiltered_ingredients = get_full_ingredients(url)
    simple_ingredients = [ i['name'] for i in og_ingredients]


    # parse directions for steps Tools, Methods, and Steps

    print("These are the parsed methods, tools, and steps. They are only printed once to help with UI.")

    methods, tools, steps = parse_directions(url,simple_ingredients)
    print( "These are the methods use in the recipe.")
    print(methods)
    print('\n' * 2)

    print("These are the tools used in the recipe.")
    print(tools)
    print('\n' * 2)

    print("There are the parsed steps:")
    num = 1

    for step in steps:
        print("This is step " + str(num) )
        pprint(step)
        print('\n' * 2)
        num += 1

    print("Press enter to continue to the main menu.")
    hold = input()


    # load in associated KB's - currently only healthy
    with open("to_health_ingredients_kb.json", 'r') as infile:
        health_kb = json.load(infile)

    with open("to_unhealth_ingredients_kb.json", 'r') as infile:
        unhealth_kb = json.load(infile)

    with open("veg_kb.json", 'r') as f:
        veg_kb = json.loads(f.read())

    with open("cuisine_kb.json", 'r') as c:
        cuisine_kb = json.loads(c.read())

    with open("cuisine_kbs/italian_kb.json", 'r') as italian:
        italian_kb = json.loads(italian.read())

    with open("cuisine_kbs/chinese_kb.json", 'r') as chinese:
        chinese_kb = json.loads(chinese.read())

    with open("cuisine_kbs/french_kb.json", 'r') as french:
        french_kb = json.loads(french.read())

    with open("cuisine_kbs/indian_kb.json", 'r') as indian:
        indian_kb = json.loads(indian.read())

    with open("cuisine_kbs/mexican_kb.json", 'r') as mexican:
        mexican_kb = json.loads(mexican.read())

    with open("cuisine_kbs/southern_us_kb.json", 'r') as southern_us:
        southern_us_kb = json.loads(southern_us.read())


    hella_recipes = pd.read_json("allrecipes-recipes.json",lines=True)



    # Core user interface
    while _continue:

        # while user wants to continue
        print('\n' * 3)
        print("MAIN MENU")
        print("Here is the parsed recipe: ")
        for ingredient in og_ingredients: print(ingredient)
        print("------------------------------------------------")



        print("Here are the original ingredients: ")
        for ingredient in unfiltered_ingredients: print(ingredient)
        print("------------------------------------------------")

        print("Here are the original directions: ")
        for direction in og_directions: print(direction)
        print("------------------------------------------------")


        # display rules for selecting transform
        print("Please select your desired transform. These are the rules we are going to display.")
        print("Select 1 to make the recipe healthy.")
        print("Select 2 to make the recepe unhealthy.")
        print("Select 3 to make the recipe vegetarian.")
        print("Select 4 to make the recipe non-vegetarian.")
        print("Select 5 to make the recipe Italian.")
        print("Select 6 to make the recipe Chinese.")
        print("Select 7 to make the recipe French.")
        print("Select 8 to make the recipe Indian.")
        print("Select 9 to make the recipe Mexican.")
        print("Select 10 to make the recipe Southern US.")

        print("Select x to quit the program. ")


        # select next action
        next = input()


        # create deep copy to ensure that original never get modified
        t_ingredients = copy.deepcopy(simple_ingredients)
        t_full_ingredients = copy.deepcopy(og_ingredients)
        t_directions = copy.deepcopy(og_directions)
        t_unfiltered = copy.deepcopy(unfiltered_ingredients)


        veg_ingredients_list = []
        for d in t_full_ingredients:
            veg_ingredients_list.append(d['quantity'] + ' ' + d['measurement'] + ' ' + d['name'])
        # call transform from imported files ------------------------------------------------------------------------



        try:

            if next == '1':
                cleaned_ingredients = health.clean_ingredients(t_ingredients,health_kb)
                new_ingredients = health.ing_swap_funtion(health_kb,cleaned_ingredients)
                new_directions = health.health_directions(cleaned_ingredients, t_directions, new_ingredients)

            if next == "2":
                cleaned_ingredients = health.clean_ingredients(t_ingredients,unhealth_kb)
                new_ingredients = health.ing_swap_funtion(unhealth_kb,cleaned_ingredients,rules_dict = "to_unhealthy" )
                new_directions = health.health_directions(cleaned_ingredients, t_directions, new_ingredients)

            if next == "3":
                new_ingredients, new_directions = vegetarian.makeVegetarian(veg_ingredients_list,t_directions,veg_kb)

            if next == "4":
                new_ingredients, new_directions = vegetarian.undoVegetarian(og_name,veg_ingredients_list,t_directions,hella_recipes,veg_kb)

            if next == "5":
                new_ingredients, og_simplified_ingredients = cuisine.to_cuisine_ingredients(t_full_ingredients, italian_kb, cuisine_kb)
                new_directions = cuisine.to_cuisine_directions(og_simplified_ingredients, t_directions, new_ingredients)

            if next == "6":
                new_ingredients, og_simplified_ingredients = cuisine.to_cuisine_ingredients(t_full_ingredients, chinese_kb, cuisine_kb)
                new_directions = cuisine.to_cuisine_directions(og_simplified_ingredients, t_directions, new_ingredients)
            if next == "7":
                new_ingredients, og_simplified_ingredients = cuisine.to_cuisine_ingredients(t_full_ingredients, french_kb, cuisine_kb)
                new_directions = cuisine.to_cuisine_directions(og_simplified_ingredients, t_directions, new_ingredients)

            if next == "8":
                new_ingredients, og_simplified_ingredients = cuisine.to_cuisine_ingredients(t_full_ingredients, indian_kb, cuisine_kb)
                new_directions = cuisine.to_cuisine_directions(og_simplified_ingredients, t_directions, new_ingredients)

            if next == "9":
                new_ingredients, og_simplified_ingredients = cuisine.to_cuisine_ingredients(t_full_ingredients, mexican_kb, cuisine_kb)
                new_directions = cuisine.to_cuisine_directions(og_simplified_ingredients, t_directions, new_ingredients)

            if next == "10":
                new_ingredients, og_simplified_ingredients = cuisine.to_cuisine_ingredients(t_full_ingredients, southern_us_kb, cuisine_kb)
                new_directions = cuisine.to_cuisine_directions(og_simplified_ingredients, t_directions, new_ingredients)

            elif next == "x":
                print("quiting the url currently being tested")
                _continue = False
                return

            new_directions = [ s.strip() for s in new_directions]


            # modify ingredients to include measurements, etc.
            if next not in ["3","4"]:
                new_ingredients = printPretty(og_ingredients,new_ingredients,t_unfiltered)
            else:
                pass # nothing needed for veg

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

            else:
                differences = findDifferences(veg_ingredients_list, new_ingredients)
                for difference in differences: print(difference)

            # write differences to file for future testing
            file = open('test.txt', "a+")
            for difference in differences:
                file.write('Change : ' + difference + '\n\n')
            file.close()


            # print the new directions
            print("----------------------------------------------------------------------")
            print(" The new directions are as follows: ")
            pprint(new_directions)

            # write new directions for testing
            file = open('test.txt', "a+")
            for direction in new_directions:
                file.write('New Direction : ' + direction + '\n\n')
            file.close()

        except:
            print('\n' * 2)
            print("There were no changes to the recipe.")
            print('\n' * 2)

        print( "Press enter to return to the main menu, otherwise enter x to exit")

        check = input()

        if check == "x":
            break

def test_internal():
    # Allows us to test multiple different urls in a row without having to read them in or try multiple



    url_italian = ['https://www.allrecipes.com/recipe/257865','https://www.allrecipes.com/recipe/23600','https://www.allrecipes.com/recipe/8669','https://www.allrecipes.com/recipe/65896']
    url_veg = ['https://www.allrecipes.com/recipe/65896','https://www.allrecipes.com/recipe/257865','https://www.allrecipes.com/recipe/23600','https://www.allrecipes.com/recipe/8669']
    url_nonveg = ['https://www.allrecipes.com/recipe/86297', 'https://www.allrecipes.com/recipe/232908', 'https://www.allrecipes.com/recipe/232908', 'https://www.allrecipes.com/recipe/60598','https://www.allrecipes.com/recipe/228241','https://www.allrecipes.com/recipe/73139']
    url_healthy = ['https://www.allrecipes.com/recipe/257865','https://www.allrecipes.com/recipe/23600','https://www.allrecipes.com/recipe/8669','https://www.allrecipes.com/recipe/65896']
    url_unhealhy = ['https://www.allrecipes.com/recipe/72381','https://www.allrecipes.com/recipe/8665','https://www.allrecipes.com/recipe/216688', 'https://www.allrecipes.com/recipe/51997']



    # What do you want to test ?
    print("-------------------------------------------------")
    print("What do you want to test?")
    print("Type: veg, nonveg, healthy, unhealthy, italian?")

    command = input()

    if command == "veg": target = url_veg
    if command == "nonveg": target = url_nonveg
    if command == "healthy": target = url_healthy
    if command == "unhealthy": target = url_unhealhy
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
    # Finds differences for veg and non veg methods
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
    # Updades ingredients to best form

    new_ingredients = []

    for index in range(0,len(old_stuff_dicts)):


        new_ing = ingredients[index]
        original = unfiltered[index]

        # check if nothing swapped or substring - if not, keep original
        if new_ing == "not_changed" or new_ing in original.lower():
            new_ingredients.append(original)

        else:
            # update with new measurement
            full_new = old_stuff_dicts[index]['quantity'] + ' ' + old_stuff_dicts[index]['measurement'] + ' ' + ingredients[index]

            new_ingredients.append(full_new)

    return new_ingredients



if __name__ == "__main__":
    #  test_internal() - This can be used for testing multiple links

    run_interface()

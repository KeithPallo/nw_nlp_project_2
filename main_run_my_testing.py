# This file can  be used for rapid autotesting our system (differences are printed)



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

# python3 -c 'import main; main.run_interface()'

# Potential for importing Jupyter notebook - have not tested this out
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from IPython.display import display, HTML
formatter = HtmlFormatter()


def run_interface(dir="empty",filename="test"):

    if dir == "empty":

        # prompt user to input a URL
        print("Please input your url.")
        url = input()

    else:
        url = dir
        print("The url being used is " + url)


    # write url to text file
    print('URL being test : ' + dir + '\n\n')


    # parse url using parse_url.py
    og_ingredients, og_directions, og_name = main_parse(url,check="single",veg="true")
    unfiltered_ingredients = get_full_ingredients(url)
    simple_ingredients = [ i['name'] for i in og_ingredients]


    # parse directions for steps Tools, Methods, and Steps
    methods, tools, steps = parse_directions(url,simple_ingredients)



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





    # while user wants to continue
    for i in range(1,11):
        next = str(i)

        print(next)

        # create deep copy to ensure that original never get modified
        t_ingredients = copy.deepcopy(simple_ingredients)
        t_full_ingredients = copy.deepcopy(og_ingredients)
        t_directions = copy.deepcopy(og_directions)
        t_unfiltered = copy.deepcopy(unfiltered_ingredients)

        veg_ingredients_list = []
        for d in t_full_ingredients:
            veg_ingredients_list.append(d['quantity'] + ' ' + d['measurement'] + ' ' + d['name'])

        try:
            # call transform from imported files ------------------------------------------------------------------------
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


                new_directions = [ s.strip() for s in new_directions]


                # modify ingredients to include measurements, etc.
                if next not in ["3","4"]:
                    new_ingredients = printPretty(og_ingredients,new_ingredients,t_unfiltered)
                else:
                    pass

                if next not in ["3","4"]:
                    differences = find_swaps(t_unfiltered,new_ingredients)
                    for different in differences: print(different)

                else:
                    differences = findDifferences(veg_ingredients_list, new_ingredients)
                    for difference in differences: print(difference)
        except:
            print("ERROR in STEP " + str(next))
            print("______________________")
            print("______________________")
            print("______________________")


    print("Clean run")


# ----------------------------------------------------------------------

# HELPER FUNCTIONS

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
        if new_ing == "not_changed" or new_ing in original.lower():
            new_ingredients.append(original)

        # UPDATE TO BETTER IMPLEMENTATION -- use parsing from unfiltered
        else:
            # update with new measurement
            full_new = old_stuff_dicts[index]['quantity'] + ' ' + old_stuff_dicts[index]['measurement'] + ' ' + ingredients[index]

            new_ingredients.append(full_new)

    return new_ingredients


if __name__ == "__main__":
    # test_internal()

    links = ["https://www.allrecipes.com/recipe/259870/briam-greek-baked-zucchini-and-potatoes/","https://www.allrecipes.com/recipe/72508/the-best-vegetarian-chili-in-the-world/","https://www.allrecipes.com/recipe/103582/seitan-in-peanut-sauce-or-vegetarian-gai-tua/","https://www.allrecipes.com/recipe/59661/spinach-enchiladas/", "https://www.allrecipes.com/recipe/simple-spinach-lasagna/", "https://www.allrecipes.com/recipe/263876/best-instant-pot-scalloped-potatoes/", "https://www.allrecipes.com/recipe/228854/all-fruit-smoothies/", "https://www.allrecipes.com/recipe/270257/zucchini-parmesan-cheese-fritters/", "https://www.allrecipes.com/recipe/25321/eggplant-parmesan-ii/", "https://www.allrecipes.com/recipe/15184/mouth-watering-stuffed-mushrooms/", "https://www.allrecipes.com/recipe/229156/zesty-quinoa-salad/", "https://www.allrecipes.com/recipe/144346/roasted-garlic-lemon-broccoli/", "https://www.allrecipes.com/recipe/165190/spicy-vegan-potato-curry/", "https://www.allrecipes.com/recipe/245208/blueberry-smoothie-bowl/", "https://www.allrecipes.com/recipe/245362/chef-johns-shakshuka/", "https://www.allrecipes.com/recipe/21528/pesto-pizza/", "https://www.allrecipes.com/recipe/254971/zavioli-with-spinach-and-ricotta/", "https://www.allrecipes.com/recipe/256728/grilled-portobello-mushrooms-with-mashed-cannellini-beans-and-harissa-sauce/", "https://www.allrecipes.com/recipe/244973/summer-bounty-pasta/", "https://www.allrecipes.com/recipe/257695/thai-rice-noodle-salad/", "https://www.allrecipes.com/recipe/255695/vegan-mexican-quinoa-bowl-with-green-chile-cilantro-sauce/", "https://www.allrecipes.com/recipe/14231/guacamole/", "https://www.allrecipes.com/recipe/49552/quinoa-and-black-beans/", "https://www.allrecipes.com/recipe/19402/quick-and-easy-alfredo-sauce/", "https://www.allrecipes.com/recipe/26692/annies-fruit-salsa-and-cinnamon-chips/", "https://www.allrecipes.com/recipe/14469/jamies-cranberry-spinach-salad/", "https://www.allrecipes.com/recipe/67952/roasted-brussels-sprouts/", "https://www.allrecipes.com/recipe/22831/alfredo-sauce/", "https://www.allrecipes.com/recipe/21261/yummy-sweet-potato-casserole/", "https://www.allrecipes.com/recipe/85452/homemade-black-bean-veggie-burgers/", "https://www.allrecipes.com/recipe/19368/chucks-favorite-mac-and-cheese/", "https://www.allrecipes.com/recipe/20669/double-tomato-bruschetta/", "https://www.allrecipes.com/recipe/54675/roasted-garlic-cauliflower/", "https://www.allrecipes.com/recipe/20876/crustless-spinach-quiche/", "https://www.allrecipes.com/recipe/33474/artichoke-spinach-dip-restaurant-style/", "https://www.allrecipes.com/recipe/26819/hot-artichoke-and-spinach-dip-ii/", "https://www.allrecipes.com/recipe/13978/lentil-soup/", "https://www.allrecipes.com/recipe/13954/addictive-sweet-potato-burritos/", "https://www.allrecipes.com/recipe/9111/cranberry-sauce/"]

    links_2 = ["https://www.allrecipes.com/recipe/15618/italian-leafy-green-salad/", "https://www.allrecipes.com/recipe/8048/italian-cream-cake-ii/", "https://www.allrecipes.com/recipe/229269/pasta-ai-fiori-di-zucca-pasta-with-zucchini-blossoms/", "https://www.allrecipes.com/recipe/246628/spaghetti-cacio-e-pepe/", "https://www.allrecipes.com/recipe/214500/sausage-peppers-onions-and-potato-bake/", "https://www.allrecipes.com/recipe/220751/quick-chicken-piccata/", "https://www.allrecipes.com/recipe/222000/spaghetti-aglio-e-olio/", "https://www.allrecipes.com/recipe/59866/modenese-pork-chops/", "https://www.allrecipes.com/recipe/255823/pasta-fazool-pasta-e-fagioli/", "https://www.allrecipes.com/recipe/246866/rigatoni-alla-genovese/", "https://www.allrecipes.com/recipe/104982/panzanella-salad/", "https://www.allrecipes.com/recipe/214164/garlic-alfredo-tilapia/", "https://www.allrecipes.com/recipe/238843/chef-johns-shrimp-fra-diavolo/", "https://www.allrecipes.com/recipe/16226/mid-summer-italian-bread-salad/", "https://www.allrecipes.com/recipe/34953/fresh-sardines-naples-style/", "https://www.allrecipes.com/recipe/6749/ciabatta/", "https://www.allrecipes.com/recipe/87389/traditional-osso-buco/", "https://www.allrecipes.com/recipe/12856/calamari/", "https://www.allrecipes.com/recipe/11890/mostaccioli-mosta/", "https://www.allrecipes.com/recipe/20568/lasagne-verdi-al-forno/", "https://www.allrecipes.com/recipe/10226/italian-anisette-cookies/", "https://www.allrecipes.com/recipe/12942/italian-sausage-soup/", "https://www.allrecipes.com/recipe/13436/italian-sausage-soup-with-tortellini/", "https://www.allrecipes.com/recipe/76129/spinach-tomato-tortellini/", "https://www.allrecipes.com/recipe/18318/pan-fried-asparagus/", "https://www.allrecipes.com/recipe/17241/biscotti/", "https://www.allrecipes.com/recipe/12918/tuscan-soup/", "https://www.allrecipes.com/recipe/13024/italian-wedding-soup-i/", "https://www.allrecipes.com/recipe/13937/pesto/", "https://www.allrecipes.com/recipe/88108/amazing-italian-lemon-butter-chicken/", "https://www.allrecipes.com/recipe/13829/roasted-garlic-mashed-potatoes/", "https://www.allrecipes.com/recipe/13028/italian-vegetable-soup/", "https://www.allrecipes.com/recipe/6955/mama-ds-italian-bread/", "https://www.allrecipes.com/recipe/18034/angel-hair-with-feta-and-sun-dried-tomatoes/", "https://www.allrecipes.com/recipe/13009/pasta-fagioli/", "https://www.allrecipes.com/recipe/154297/italian-cream-cheese-and-ricotta-cheesecake/", "https://www.allrecipes.com/recipe/72567/panna-cotta/", "https://www.allrecipes.com/recipe/15618/italian-leafy-green-salad/", "https://www.allrecipes.com/recipe/8048/italian-cream-cake-ii/", "https://www.allrecipes.com/recipe/229269/pasta-ai-fiori-di-zucca-pasta-with-zucchini-blossoms/", "https://www.allrecipes.com/recipe/246628/spaghetti-cacio-e-pepe/", "https://www.allrecipes.com/recipe/214500/sausage-peppers-onions-and-potato-bake/", "https://www.allrecipes.com/recipe/220751/quick-chicken-piccata/", "https://www.allrecipes.com/recipe/222000/spaghetti-aglio-e-olio/", "https://www.allrecipes.com/recipe/59866/modenese-pork-chops/", "https://www.allrecipes.com/recipe/246866/rigatoni-alla-genovese/", "https://www.allrecipes.com/recipe/255823/pasta-fazool-pasta-e-fagioli/", "https://www.allrecipes.com/recipe/104982/panzanella-salad/", "https://www.allrecipes.com/recipe/214164/garlic-alfredo-tilapia/", "https://www.allrecipes.com/recipe/238843/chef-johns-shrimp-fra-diavolo/", "https://www.allrecipes.com/recipe/9947/pizzelles-ii/", "https://www.allrecipes.com/recipe/16226/mid-summer-italian-bread-salad/", "https://www.allrecipes.com/recipe/34953/fresh-sardines-naples-style/", "https://www.allrecipes.com/recipe/6749/ciabatta/", "https://www.allrecipes.com/recipe/87389/traditional-osso-buco/", "https://www.allrecipes.com/recipe/12856/calamari/", "https://www.allrecipes.com/recipe/11890/mostaccioli-mosta/", "https://www.allrecipes.com/recipe/20568/lasagne-verdi-al-forno/", "https://www.allrecipes.com/recipe/10226/italian-anisette-cookies/", "https://www.allrecipes.com/recipe/12942/italian-sausage-soup/", "https://www.allrecipes.com/recipe/13436/italian-sausage-soup-with-tortellini/", "https://www.allrecipes.com/recipe/76129/spinach-tomato-tortellini/", "https://www.allrecipes.com/recipe/18318/pan-fried-asparagus/", "https://www.allrecipes.com/recipe/17241/biscotti/", "https://www.allrecipes.com/recipe/12918/tuscan-soup/", "https://www.allrecipes.com/recipe/13024/italian-wedding-soup-i/", "https://www.allrecipes.com/recipe/13937/pesto/", "https://www.allrecipes.com/recipe/88108/amazing-italian-lemon-butter-chicken/", "https://www.allrecipes.com/recipe/13829/roasted-garlic-mashed-potatoes/", "https://www.allrecipes.com/recipe/13028/italian-vegetable-soup/", "https://www.allrecipes.com/recipe/6955/mama-ds-italian-bread/", "https://www.allrecipes.com/recipe/18034/angel-hair-with-feta-and-sun-dried-tomatoes/", "https://www.allrecipes.com/recipe/13009/pasta-fagioli/", "https://www.allrecipes.com/recipe/154297/italian-cream-cheese-and-ricotta-cheesecake/", "https://www.allrecipes.com/recipe/72567/panna-cotta/"]

    for link in links:
        run_interface(link)


# load in standard libraries
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

# load in nltk for
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams


# load in module functions
import healthy

# python3 -c 'import main; main.run_interface()'

# Potential for importing Jupyter notebook - have not tested this out
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from IPython.display import display, HTML
formatter = HtmlFormatter()


def run_interface():

    continue = True

    # prompt user to input a URL
    print("Please input your url.")
    url = input()


    # parse url using parse_url.py
    og_ingredients, og_directions = main_parse(url,check="single")

    # write original to text file
    # TO DO

    # load in associated KB's - currtently only healthy

    with open("to_health_ingredients_kb.json", 'r') as infile:
        health_kb = json.load(infile)

    while continue:
        # while user wants to continue


        # display original recipe
        pprint(og_ingredients)
        pprint(og_directions)


        # display rules for selecting transform
        print("These are the rules we are going to display. Select 1 for healthy, and x to quick")

        # select next action
        next = input()

        # call transform from imported files

        if next == '1':

            # create deep copy to ensure that original never get modified
            t_ingredients = copy.deepcopy(og_ingredients)
            t_ingredients = copy.deepcopy(og_ingredients)

            # select transform based on input
            cleaned_ingredients = healthy.clean_ingredients(og_ingredients,health_kb)
            new_ingredients = healthy.ing_swap_funtion(rule_dict,health_kb,cleaned_ingredients)
            # TO DO - write cleaned directions

        elif next == "x":
            print("quiting the url currently being tested")
            continue = False
            return



        # print new recipe
        pprint(new_ingredients)


        # print differences using diff_for_display
        # TO DO - Write function


        # TO DO - write transform to txt file for later processing

def test_internal():

    # read in list of URLS


    # call run interface with optional parameter to input parameter


def display_standard():
    # display ingredients for the user

def diff_for_display(original_list,old_list):
    # after printing the new version - use this to display the


def parse_ingredients():
    pass


if __name__ == "__main__":
    # test_interal() - change this to select a specific type of ingredient list

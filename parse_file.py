# running python version 3.6

#import utils
import os, sys
import bs4 as bs
import urllib.request
import json
from ingredient_parser import en


def main_parse(url_passed,check ="single",url_name = "test"):
    """
    url_passed type = string
    """

    # Read in KB's
    file = open("CookingTechniques.json", "r")
    cooking = json.load(file)
    cooking = set(cooking)

    file = open("KitchenUtensils.json", "r")
    utensils = json.load(file)
    utensils = set(utensils)

    # Soupify the url
    source = urllib.request.urlopen(url_passed).read()
    soup = bs.BeautifulSoup(source,'lxml')
    body = soup.body

    # Make empty lists for extraction
    ingredients = []
    prep = []
    directions = []


    for div in body.find_all(class_='recipe-ingred_txt added'):
        string = div.text
        # Insert cleaning for ingredients
    	# Currently using API from raw import
        ing_dict = en.parse(string)
        output_string = str(ing_dict)
        ingredients.append(output_string)



    for div in body.find_all(class_='prepTime__item'):
    	if div.text != "":
    		prep.append(div.text)


    for div in body.find_all(class_='recipe-directions__list--item'):
    	if div.text != "":
            string = div.text
            string = string.split()
            directions.extend(string)

    # Instanciate Found
    id_cooking = []
    id_utensils = []

    # Split Ingredients into Name, Quantity, Measurement
    # To do

    # Extract cooking and utensils
    for word in directions:

        if word in cooking:  # potentially remove duplicates
            id_cooking.append(word)
        if word in utensils: # potentially remove duplicates
            id_utensils.append(word)

    # Check if single_recipe
    if check == "single":
        write_single_repcipe(url_name,ingredients,id_cooking,id_utensils)

    else:
        write_testing(url_name,ingredients,id_cooking,id_utensils)




def write_single_repcipe(url_name,ingredients,id_cooking,id_utensils):

    f = open(url_name, 'a+')
    f.write('Ingredients: ' + ', '.join(ingredients) + '\n\n')
    f.write('Cooking Techniques: ' + ', '.join(id_cooking) + '\n\n') # This will need to change
    f.write('Utensils Used: ' + ', '.join(id_utensils) + '\n\n')


def write_testing(url_name,ingredients,id_cooking,id_utensils):

    ing_name = url_name + "ingredients.json"
    with open(ing_name, 'a+') as outfile:
        json.dump(ingredients, outfile)

    cook_name = url_name + "cooking.json"
    with open(cook_name, 'a+') as outfile:
        json.dump(id_cooking, outfile)

    uten_name = url_name + "utensils.json"
    with open(uten_name, 'a+') as outfile:
        json.dump(id_utensils, outfile)

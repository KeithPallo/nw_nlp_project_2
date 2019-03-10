# running python version 3.6

#import utils
import os, sys
import bs4 as bs
import urllib.request
import json
import ing_parser

# python3 -c 'import parse_url; parse_url.main_parse('https://www.allrecipes.com/recipe/228293')'



def main_parse(url_passed,check ="single",url_name = "test"):
    """
    url_passed type = string
    """

    url_name = "test_" + str(url_passed) + ".txt"
    # url_name += ".txt"

    # Read in KB's
    file = open("kb_files/CookingTechniques.json", "r")
    cooking = json.load(file)
    cooking = set(cooking)

    file = open("kb_files/KitchenUtensils.json", "r")
    utensils = json.load(file)
    utensils = set(utensils)

    # Soupify the url
    source = urllib.request.urlopen(url_passed).read()
    soup = bs.BeautifulSoup(source,'lxml')
    body = soup.body

    # Make empty lists for extraction
    ingredients = []
    full_ingredients = []
    prep = []
    directions = []


    for div in body.find_all(class_='recipe-ingred_txt added'):
        string = div.text
        # Insert cleaning for ingredients
    	# Currently using API from raw import

        ing_dict = ing_parser.parse(string)
        # print(type(ing_dict))
        # Check for type of output
        if check == "single":
            output_string = ing_dict
            ingredients.append(output_string)

        else:
            output_string = ing_dict
            ingredients.append(output_string)


    for div in body.find_all(class_='prepTime__item'):
    	if div.text != "":
    		prep.append(div.text)


    for div in body.find_all(class_='recipe-directions__list--item'):
    	if div.text != "":
            string = div.text
            directions.append(string)

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
        # write_single_recipe(url_name,ingredients,id_cooking,id_utensils)
        return ingredients, directions

    else:
        write_testing(url_name,ingredients,id_cooking,id_utensils)


def get_full_ingredients(url_passed):

    # Soupify the url
    source = urllib.request.urlopen(url_passed).read()
    soup = bs.BeautifulSoup(source,'lxml')
    body = soup.body

    # Make empty lists for extraction

    full_ingredients = []


    for div in body.find_all(class_='recipe-ingred_txt added'):
        string = div.text
        full_ingredients.append(string)

    return full_ingredients






def write_single_recipe(url_name,ingredients,id_cooking,id_utensils):

     with open(url_name, 'w') as f:  #

        str_ingredients = str(ingredients)
        str_id_cooking = str(id_cooking)
        str_id_utensils = str(id_utensils)

        f.write('Ingredients: ' + ', '.join(str_ingredients) + '\n\n')
        f.write('Cooking Techniques: ' + ', '.join(str_id_cooking) + '\n\n') # This will need to change
        f.write('Utensils Used: ' + ', '.join(str_id_utensils) + '\n\n')




def write_testing(url_name,ingredients,id_cooking,id_utensils):

    # Build Ingredients File
    ing_name = url_name + "ingredients.json"

    try:
        with open(ing_name, 'r') as outfile:
            prev = json.load(outfile)
        prev.extend(ingredients)
        ingredients = prev

    except:
        pass

    with open(ing_name, 'w') as outfile:
        json.dump(ingredients, outfile)

    # Build Cooking File
    cook_name = url_name + "cooking.json"
    try:
        with open(cook_name, 'r') as outfile:
            prev = json.load(outfile)
        prev.extend(id_cooking)
        id_cooking = prev

    except:
        pass

    with open(cook_name, 'w') as outfile:
        json.dump(id_cooking, outfile)


    # Build Utensils File
    uten_name = url_name + "utensils.json"

    try:
        with open(uten_name, 'r') as outfile:
            prev = json.load(outfile)
        prev.extend(id_utensils)
        id_utensils = prev

    except:
        pass

    with open(uten_name, 'w') as outfile:
        json.dump(id_utensils, outfile)


# if __name__ == "__main__":

    #ingredients, directions = main_parse('https://www.allrecipes.com/recipe/228293')

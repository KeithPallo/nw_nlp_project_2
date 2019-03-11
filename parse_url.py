# running python version 3.6

#import utils
import os, sys
import bs4 as bs
import urllib.request
import json
import ing_parser
from pprint import pprint

# load in nltk for
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re

# python3 -c 'import parse_url; parse_url.main_parse('https://www.allrecipes.com/recipe/228293')'



def main_parse(url_passed,check ="single",url_name = "test"):
    """
    url_passed type = string
    """

    url_name = "test_" + str(url_passed) + ".txt"

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

        # Clean the string with import
        ing_dict = ing_parser.parse(string)

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


    # Check if single_recipe
    if check == "single":
        # write_single_recipe(url_name,ingredients,id_cooking,id_utensils)
        return ingredients, directions

    else:
        write_testing(url_name,ingredients,id_cooking,id_utensils)





def parse_directions(url_passed,ingredients = None):
    # Return methods, tools, and steps

    # Ingredients can be any of the type ingredients that we are passing in


    directions = []

    url_name = "test_" + str(url_passed) + ".txt"

    # Read in KB's
    file = open("kb_files/CookingTechniques.json", "r")
    methods = json.load(file)
    methods= set(methods)
    file.close()

    file = open("kb_files/KitchenUtensils.json", "r")
    tools = json.load(file)
    tools = set(tools)
    file.close()


    url_name = "test_" + str(url_passed) + ".txt"

    # Soupify the url
    source = urllib.request.urlopen(url_passed).read()
    soup = bs.BeautifulSoup(source,'lxml')
    body = soup.body

    # Get the directions
    for div in body.find_all(class_='recipe-directions__list--item'):
    	if div.text != "":
            string = div.text
            directions.append(string)

    print("look here")
    pprint(len(directions))

    # Instanciate lists for Tools (cooking) and Methods (utensils )
    id_methods = []
    id_tools = []


    # Split ingredients into words for testing

    split_directions = [words for segments in directions for words in segments.split()]

    # Extract cooking and utensils
    for word in split_directions:
        #print(word)

        if word in methods:  # potentially remove duplicates
            id_methods.append(word)
        if word in tools: # potentially remove duplicates
            id_tools.append(word)

    # Full list of methods and tools
    id_methods = list(set(id_methods))
    id_tools = list(set(id_tools))

    # Parse each ingredient individually

    step_number = 1
    empty = { }

    steps = []

    # make everygram from ingredients

    ingredient_grams = get_ngrams(ingredients)
    ingredients_search = list(zip(ingredients, ingredient_grams))

    for direction in directions:

        step = {
		"times" : [],
		"ingredients" : [],
		"methods" : [],
		"tools" : []}

        # split the directions
        split_single = direction.split()

        # Find Methods and tools
        # print(split_single)
        for word in split_single:
            # print(type(word))
            if word in methods:
                if word not in step['methods']:
                    step['methods'].append(word)
            if word in tools:
                if word not in step['tools']:
                    step['tools'].append(word)

        # find the times
        times = get_times(direction)
        step['times'].extend(times)

        # find the ingredients
        for ingredient_tup in ingredients_search:
            # print(ingredient_tup)
            original = ingredient_tup[0]
            permuations = ingredient_tup[1]

            for perm in permuations:
                if perm in direction:
                    step["ingredients"].append(original)
                    break

        # append the step
        steps.append(step)


    return id_methods, id_tools, steps



def get_ngrams(i_list):
    all_grams = []

    for i in i_list:
        l = clean_text(i)
        grams = list(nltk.everygrams(l, max_len=len(l)))
        grams.sort(key=len, reverse=True)
        grams = [' '.join(g) for g in grams]
        all_grams.append(grams)

    return all_grams


def clean_text(s):
    # import stop words
    stop_words = set(stopwords.words('english'))

    s = re.sub("[^a-zA-Z ]", ' ', s)
    s = s.lower()
    s = word_tokenize(s)

    # filter out stop words
    words = [w for w in s if not w in stop_words]

    return words


def get_times(og_direction):
    times = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours']
    direction_times = []
    tokenized = nltk.word_tokenize(og_direction)
    for i in tokenized:
        if i in times:
            idx = tokenized.index(i)
            if tokenized[idx-1]:
                direction_times.append(tokenized[idx-1]+' '+i)

    return direction_times


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


if __name__ == "__main__":

    methods, tools = parse_directions('https://www.allrecipes.com/recipe/228293')

    print("The tools used are:")
    pprint(tools)

    print("The methods used are:")
    pprint(methods)

    #ingredients, directions = main_parse('https://www.allrecipes.com/recipe/228293')

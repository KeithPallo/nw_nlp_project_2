import pandas as pd
import nltk

# To make dish vegetarian call
#   makeVegetarian(ingredients, directions, kb):
#
#       inputs: - list of ingredients as strings
#               - list of directions as strings
#               - food kb (needs keys 'meats', 'poultry', 'fish', and 'seafood')
#
#       outputs: - list of new ingredients as strings
#                - list of new directions as strings
#
#
# To undo vegetarian call
#   undoVegetarian(dish_name, ingredients, directions, hella_recipes):
#
#       inputs: - dish name as a string
#               - list of ingredients as strings
#               - list of directions as strings
#               - recipe kb (hella_recipes = pd.read_json("allrecipes-recipes.json",lines=True)
#
#       outputs: - list of new ingredients as strings
#                - list of new directions as strings
#
#
# To output differences in two lists call
#   findDifferences(old_ingredients, new_ingredients):
#
#       inputs: - old list with with strings
#               - new list with with strings
#
#       outputs: - list of strings where each string is either
#                   - 'ingredient -> removed'
#                   - 'added' -> ingredient'



# Normal -> Vegetarian
#
# inputs: - list of ingredients as strings
#         - list of directions as strings
#         - food kb (needs keys 'meats', 'poultry', 'fish', and 'seafood')
#
# outputs: - list of new ingredients as strings
#          - list of new directions as strings
def makeVegetarian(ingredients, directions, kb):
    Substitutions = {'meats':{'ingredients':['1 lb extra-firm tofu, drained',
                                             '1 tablespoon dark sesame oil, divided',
                                             '1 tablspoon soy sauce'],
                                             #1 cup julienne-cut red bell pepper',
                                             #'1 cup matchstick-cut carrot',
                                             #'1/8 teaspoon salt',
                                             #'4 garlic cloves, thinly sliced',
                                             #'1 (5-ounce) package presliced shiitake mushrooms',
                                             #'1/2 cup organic vegetable broth',
                                             #'1 tablespoon honey',
                                             #'2 teaspoons sherry vinegar',
                                             #'1/2 teaspoon crushed red pepper',
                                             #'Cooking spray],
        'directions':['Cut tofu in half crosswise and again in half lengthwise.',
                      'Pierce tofu liberally with a fork. Place in a shallow dish.',
                      'Combine 1 tablespoon oil and 1 tablespoon soy sauce in a small bowl.',
                      'Pour soy mixture over tofu; let stand 15 minutes, turning once. Set aside.']},
                      #''''Heat a large nonstick skillet over medium-high heat.',
                      #'Add 1 tablespoon oil; swirl to coat.',
                      #'Add bell pepper, carrot, and salt; sauté 3 minutes.',
                      #'Remove from pan.',
                      #'Add remaining 1 tablespoon oil; swirl to coat.',
                      #'Add garlic and mushrooms; sauté 4 minutes.',
                      #'Add remaining 2 tablespoons soy sauce, broth, and next 3 ingredients.',
                      #'Simmer 3 minutes or until thickened.',
                      #'Remove from heat.',
                      #'Remove tofu from marinade; reserve marinade.',
                      #'Heat a grill pan over high heat.',
                      #'Coat pan with cooking spray.',
                      #'Add tofu to pan; cook 3 minutes on each side, basting occasionally with reserved marinade.',
                      #'Arrange 1 tofu steak on each of 4 plates; top each serving with about 1/3 cup carrot mixture and about 2 tablespoons mushroom mixture.''']},
            'poultry':{'ingredients':['2 blocks firm or extra-firm tofu, well pressed',
                                      '2 tbsp. soy sauce',
                                      '2 tbsp. lemon juice',
                                      '2 tbsp. olive oil',
                                      '2 tbsp. Dijon mustard',
                                      '1 tsp. sugar',
                                      '1 tsp. basil',
                                      '1 tsp. thymeSalt and pepper to taste'],
                'directions':['First, prepare your tofu. Like most tofu recipes, tofu scramble will taste best if you press the tofu first. This allows the tofu to absorb more of the flavorings and seasonings which you add to it. Its an extra step, but it just takes a few minutes.',
                              'Slice your pressed tofu into 1/2-inch thick strips.',
                              'Whisk together all ingredients except for tofu. Transfer to a shallow pan or zipped plastic bag then the tofu, coating well.',
                              'Allow tofu to marinate for at least one hour (the longer the better, turning to coat well with marinade).']},
                    #'''"Heat oven to 375 F.",
                    #"Transfer tofu and marinade to baking dish and bake for 20 to 25 minutes, turning halfway through and pouring extra marinade over the tofu as needed."''']},
                    'fish':{'ingredients':['2 tablespoons of oil',
                                           '2 slabs of tempeh',
                                           '1 tablespoon of Old Bay Seasoning',
                                           '1 lemon',
                                           'Add seaweed as desired'],
                        'directions':[#'''put oil in pan',
                                      #'place tempeh in pan'''
                                      'Season tempeh with old bay seasoning, lemon, and chopped up pieces of seaweed']},
                                      #'''cook 3-5 min each side until lightly browned''']},
                            'seafood':{'ingredients':['1/4 cup extra-virgin olive oil',
                                                      '6 garlic cloves, minced',
                                                      'Zest and juice of one lemon',
                                                      '1 tablespoon Old Bay Seasing',
                                                      'Salt and pepper, to taste'],
                                'directions':['In a bowl, combine the ingredients for the marinade.',
                                              'Let the “shrimp” or tofu sit in the marinade for at least 30 minutes']}}
                                              #'''Heat a large skillet over medium-high heat. Remove the “shrimp” or tofu from the marinade, shake off any excess and place them in the skillet.',
                                              #'Cook for about 4-6 minutes or until they have browned a bit on all sides, according to your taste.',
                                              #'Remove the “shrimp” or tofu from the skillet and set aside''']}}

    clean_ingredients = []
    clean_directions = []
    non_vegetarian = []

    for ingredient in ingredients:
        if any(term in ingredient for term in kb['meats']):
            if Substitutions['meats']['ingredients'][0] not in clean_ingredients:
                clean_ingredients += Substitutions['meats']['ingredients']
                clean_directions += Substitutions['meats']['directions']
                non_vegetarian += kb['meats']
                meat_sub = 'tofu'

        elif any(term in ingredient for term in kb['poultry']):
            if Substitutions['poultry']['ingredients'][0] not in clean_ingredients:
                clean_ingredients += Substitutions['poultry']['ingredients']
                clean_directions += Substitutions['poultry']['directions']
                non_vegetarian += kb['poultry']
                meat_sub = 'tofu'

        elif any(term in ingredient for term in kb['fish']):
            if Substitutions['fish']['ingredients'][0] not in clean_ingredients:
                clean_ingredients += Substitutions['fish']['ingredients']
                clean_directions += Substitutions['fish']['directions']
                non_vegetarian += kb['fish']
                meat_sub = 'tempeh'

        elif any(term in ingredient for term in kb['seafoods']):
            if Substitutions['seafoods']['ingredients'][0] not in clean_ingredients:
                clean_ingredients += Substitutions['seafoods']['ingredients']
                clean_directions += Substitutions['seafoods']['directions']
                non_vegetarian += kb['seafoods']
                meat_sub = 'tofu'

        else:
            clean_ingredients.append(ingredient)

    '''for step in directions:
        if not any(term in step for term in kb['meats']) and not any(term in step for term in kb['poultry']) and not any(term in step for term in kb['fish']) and not any(term in step for term in kb['seafoods']) and 'meat' not in step:
            clean_directions.append(step)'''

    for step in directions:
        #vegan = False
        for word in step.split():
            for not_allowed in non_vegetarian:
                if not_allowed in word:
                    step = step.replace(word,  meat_sub)
            #if not vegan:
        clean_directions.append(step)

    return clean_ingredients, clean_directions


# helper function to undoVegetarian
def findMeat(dish_name, ingredients, directions, hella_recipes, new_kb):

    some_recipes = pd.DataFrame()
    found_vegetarian = False
    normal_name = ''

    for word in dish_name.split():
        if found_vegetarian:
            word[0].upper()
            normal_name += word
            normal_name += ' '

        if word.lower() == 'vegetarian':
            found_vegetarian = True

    if found_vegetarian:
        some_recipes = hella_recipes[hella_recipes['title'].str.contains(normal_name)]

    else:
        split_name = dish_name.split()
        for word in split_name:
            some_recipes = some_recipes.append(hella_recipes[hella_recipes['title'].str.contains(word)])

    some_recipes = some_recipes['ingredients'].values

    ingredients_list = []

    for ing_list in some_recipes:
        for word in ing_list:
            if any(term in word.lower() for term in new_kb['meats']) or any(term in word.lower() for term in new_kb['poultry']) or any(term in word.lower() for term in new_kb['fish']) or any(term in word.lower() for term in new_kb['seafoods']):
                ingredients_list.append(word.lower())

    ingredients_grams = []

    for ingredient in ingredients_list:
        gram = list(nltk.everygrams(ingredient.split()))

        for g in gram:
            if len(g) > 1:
                ingredients_grams.append(' '.join(g))
            else:
                ingredients_grams.append(g[0])

    ingredients_dist = nltk.FreqDist(ingredients_grams)

    return ingredients_dist.most_common()


# helper function to undoVegetarian
def replaceInSubstitutions(insert, meat_dict):
    ingredients_list = []
    directions_list = []

    for ingredient in meat_dict['ingredients']:
        if 'replace_this' in ingredient:
            ingredient = ingredient.replace("replace_this", insert)
        ingredients_list.append(ingredient)

    for step in meat_dict['directions']:
        if 'replace_this' in step:
            step = step.replace("replace_this", insert)
        directions_list.append(step)

    return ingredients_list, directions_list


# Vegetarian -> Normal
#
# inputs: - dish name as a string
#         - list of ingredients as strings
#         - list of directions as strings
#         - recipe kb (hella_recipes = pd.read_json("allrecipes-recipes.json",lines=True)
#
# outputs: - list of new ingredients as strings
#          - list of new directions as strings
def undoVegetarian(dish_name, ingredients, directions, hella_recipes,new_kb):

    Substitutions = {'meats': {'ingredients': ['1 lb replace_this',
                                               '1/2 cup of red wine',
                                               '1 tablespoon Dijon Mustard',
                                               '1 tablespoon olive oil',
                                               '1 freshly ground pepper',
                                               'A pinch of thyme'],
        'directions': ['Marinate the replace_this for 6 to 12 hours in a mixture of red wine, Dijon mustard, olive oil, freshly ground pepper and thyme.',
                       'Remove the replace_this from the marinade and pat dry with paper towels.']},
                       #'Place on the rack of a roasting pan.',
                       #'Place the pan in a 230°C (450°F) oven.',
                       #'Cook for 10 to 12 minutes, depending on the thickness of the replace_this.',
                       #'After cooking, remove from oven and cover loosely with aluminum foil, allowing heat to escape. Let stand for 5 to 8 minutes before serving.']},
            'poultry': {'ingredients': ['2 boneless, skinless chicken breasts (about 1 pound total)',
                                        '3/4 teaspoon kosher salt',
                                        '1/4 teaspoon freshly ground black pepper'],
                                        #'2 tablespoons canola oil',
                                        #'1 tablespoon unsalted butter or ghee',
                'directions': ['Pat the chicken dry and season with salt and pepper.Thoroughly dry the chicken on all sides with paper towels. Season with the salt and pepper on all sides.']},
                               #'Heat the oil over medium-high heat in a large skillet. Heat the oil in a 10-inch or larger skillet, preferably straight-sided and not nonstick (cast iron is a great option), over medium-high heat until shimmering, about 3 minutes.',
                               #'Carefully add the chicken to the hot pan and cook for 5 to 7 minutes. Swirl the pan just before adding the breasts to evenly distribute the oil. Add the chicken one at a time and do not touch, poke, or move the chicken for 5 to 7 minutes. If you try to turn the chicken and it feels stuck, it isnt golden and crispy or ready to flip.',
                               #'Flip the chicken and cook until it reaches 165°F, 5 to 7 minutes more. Flip the breasts over and add the butter or ghee right between them. Pick up the pan and give it a gentle swirl to distribute the melting butter. Cook until they reach an internal temperature of 165°F, 5 to 7 minutes more.',
                               #'Slice and serve. Remove the chicken breasts to a plate or clean cutting board. Let rest for 3 minutes before slicing and serving.']},
                    'fish': {'ingredients': ['1 6- to 8-ounce replace_this fillet per person',
                                             'Salt and pepper to taste'],
                                             #'2 tablespoons olive oil or butter',
                                             #'To serve: lemon wedges, minced herbs, capers, etc.'],
                        'directions': ['Pat the fish dry: Use a paper towel to pat the fish dry on both sides.',
                                       'Sprinkle with salt and pepper: Sprinkle the top of the fish generously with salt and pepper.']},
                                       #'Warm the oil in the skillet: Warm the olive oil or butter in a skillet over medium-high heat. The pan is ready when a flick of water sizzles on contact with the pan.',
                                       #'Lay the fish in the hot pan: Lay the fish, seasoned-side down, in the pan.',
                                       #'Cook for 2 to 3 minutes: Cook the fish for 2 to 3 minutes without moving it. When ready to flip, the underside should look golden and crispy. It should also release fairly easily from the pan using a fish spatula. (Not a problem in an non-stick skillet!)  Season the other side of the fish: While the first side cooks, season the other side with salt and pepper.',
                                       #'Flip the fish and cook for another 2 to 3 minutes: Flip the fish to the second side and cook for another 2 to 3 minutes. When ready, the fish will be opaque all the way through and flake apart easily.',
                                       #'Serve immediately: Serve the fish while still hot from the pan with any finishing garnishes. White fish can often be very flaky after cooking; dont worry if it flakes apart a bit as you serve it.']},
                            'seafood': {'ingredients': ['1 pound raw replace_this (17 to 21 per pound)',
                                                        #'1 tablespoon olive oil or butter, or a mix',
                                                        'Kosher salt to taste',
                                                        'Freshly ground black pepper to taste'],
                                'directions': ['If your replace_this are frozen, place them in a colander in the sink and run cold water over them for about 5 minutes. Toss the replace_this occasionally to make sure they are all exposed to the cold water.',
                                               'The replace_this is thawed and ready when they are no longer frozen solid but soft, easily bendable, and slightly translucent. This will only take a few minutes. Pat the replace_this dry with paper towels.',
                                               'Generously season replace_this with salt and pepper']}}
                                               #'Place the oil or butter in a large frying pan over medium-high heat. Tilt the pan as the oil warms, or butter melts, to coat the bottom of the pan.',
                                               #'When the butter is melted or the oil moves around the pan easily, add the replace_this. They should sizzle on contact (if not, warm your pan a little longer next time).',
                                               # 'Sprinkle salt and pepper over the replace_this. Be generous! You can also add any other seasonings at this point — chili spice, curry spice, a bit of harissa, or any other seasonings in your cupboard.',
                                               #'Serve sautéed replace_this immediately']}}

    vegetarian_foods = ['tofu', 'tempeh', 'seitan', 'vegan meat', 'jackfruit', 'mushroom', 'mushrooms', 'vegetarian']

    clean_ingredients = []
    clean_directions = []

    possible_meats = findMeat(dish_name, ingredients, directions, hella_recipes, new_kb)
    new_meat = 'beef'
    ingredients_to_add, directions_to_add = replaceInSubstitutions(new_meat, Substitutions['meats'])

    for meat in possible_meats:
        if any(term == meat for term in new_kb['meats']):
            new_meat = meat
            ingredients_to_add, directions_to_add = replaceInSubstitutions(new_meat, Substitutions['meats'])
            break

        if any(term == meat for term in new_kb['poultry']):
            new_meat = meat
            ingredients_to_add, directions_to_add = replaceInSubstitutions(new_meat, Substitutions['poultry'])
            break

        if any(term == meat for term in new_kb['fish']):
            new_meat = meat
            ingredients_to_add, directions_to_add = replaceInSubstitutions(new_meat, Substitutions['fish'])
            break

        if any(term == meat for term in new_kb['seafoods']):
            new_meat = meat
            ingredients_to_add, directions_to_add = replaceInSubstitutions(new_meat, Substitutions['seafoods'])
            break

    clean_ingredients += ingredients_to_add

    for ingredient in ingredients:
        vegan = False
        for word in ingredient.split():
            for not_allowed in vegetarian_foods:
                if not_allowed in word:
                    vegan = True
        if not vegan:
            clean_ingredients.append(ingredient)


    clean_directions += directions_to_add

    for step in directions:
        #vegan = False
        for word in step.split():
            for not_allowed in vegetarian_foods:
                if not_allowed in word:
                    step = step.replace(word, new_meat)
        #if not vegan:
        clean_directions.append(step)

    return clean_ingredients, clean_directions


# Takes two lists, old and new, and outputs differences between old and new
#
# inputs: - old list with with strings
#         - new list with with strings
#
# outputs: - list of differences

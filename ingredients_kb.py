#!/usr/bin/env python
# coding: utf-8

# In[3]:


import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.allrecipes.com/recipe/228293/curry-stand-chicken-tikka-masala-sauce/?internalSource=hub%20recipe&referringContentType=Search').read()

soup = bs.BeautifulSoup(source,'lxml')

body = soup.body

for div in body.find_all(class_='recipe-ingred_txt added'):
    print(div.text)

print("next_sec")

test_prep = []

for div in body.find_all(class_='prepTime__item'):
    if div.text != "":
        test_prep.append(div.text)

print(test_prep)

test_directions = []

for div in body.find_all(class_='recipe-directions__list--item'):
    if div.text != "":
        test_directions.append(div.text)

print("Next Test Section")
print()
print(test_directions)


# In[14]:


f = open("KitchenUtensils.txt", "r")

kitchenUtensils = []

for utensil in f:
    no_new_line = utensil.split('\n')
    kitchenUtensils.append(no_new_line[0].lower())
    
print(kitchenUtensils[1:])


# In[16]:


f = open("KitchenUtensils.txt", "r")

kitchenUtensils = []

for utensil in f:
    no_new_line = utensil.split('\n')
    if len(no_new_line[0]) > 1:
        kitchenUtensils.append(no_new_line[0].lower())
    
print(kitchenUtensils[1:])


# In[18]:


one = ['baking dish', 'baking tray', 'cake pan', 'can opener', 'chopping board', 'coffee press', 'colander', 'cooling rack', 'corkscrew', 'cutlery', 'dinnerware', 'eggbeater', 'egg slicer', 'electric mixer', 'fork', 'frying pan', 'garlic press', 'grater', 'glassware', 'grill pan', 'kitchen scissors', 'knives', 'mandolin', 'measuring cups and spoons', 'measuring spoon', 'meat slicer', 'mixing bowls', 'muffin tin', 'pasta server', 'peeler', 'pepper mill', 'pie dish', 'pizza stone', 'plates', 'potato masher', 'potato ricer', 'rolling pin', 'saucepan', 'serving fork', 'serving spoon', 'sheet pan', 'skillet', 'slotted spoon', 'soup spoon', 'spatula', 'spiral vegetable slicer', 'spoon', 'stock pot', 'steamers', 'strainer', 'timer', 'tomato slicer', 'tongs', 'tray', 'whisk', 'wok', 'wooden spoon']
two = ['air fryer', 'auto reignition', 'bachelor griller', 'barbecue', 'barbecue grill', 'big green egg', 'brasero (heater)', 'brazier', 'bread machine', 'broaster company', 'brown bobby', 'burjiko', 'butane torch', 'charbroiler', 'cheesemelter', 'chocolatera', 'coffee percolator', 'coffeemaker', 'comal (cookware)', 'combi steamer', 'cooker', 'list of cooking appliances', 'cooktop', 'corn roaster', 'crepe maker', 'deep fryer', 'electric cooker', 'field kitchen', 'fire pot', 'flattop grill', 'food steamer', 'footman (furniture)', 'fufu machine', 'halogen oven', 'haybox', 'horno', 'hot box (appliance)', 'hot plate', 'induction cooking', 'instant pot', 'kamado', 'kettle', 'kitchener range', 'krampouz', 'kujiejun', 'kyoto box', 'mess kit', 'multicooker', 'oven', 'pancake machine', 'pie iron', 'popcorn maker', 'pressure cooking', 'pressure frying', 'remoska', 'rice cooker', 'rice polisher', 'roasting jack', 'rocket mass heater', 'rollie eggmaster', 'rotisserie', 'sabbath mode', 'salamander broiler', 'samovar', 'shichirin', 'siru', 'slow cooker', 'solar cooker', 'soy milk maker', 'stove', 'susceptor', 'tandoor', 'thermal cooking', 'thermal immersion circulator', 'thermomix', 'toaster', 'trojan room coffee pot', 'turkey fryer', 'vacuum fryer', 'waffle iron', 'wet grinder', 'wet grinder (food)', 'whistling kettle']

for i in one:
    if i not in two:
        two.append(i)
        
print(two)


# In[19]:


f = open("KitchenUtensils.txt", "r")

kitchenUtensils = []

for utensil in f:
    no_new_line = utensil.split('\n')
    if len(no_new_line[0]) > 1:
        kitchenUtensils.append(no_new_line[0].lower())
    
print(kitchenUtensils[1:])


# In[23]:


one = ['air fryer', 'auto reignition', 'bachelor griller', 'barbecue', 'barbecue grill', 'big green egg', 'brasero (heater)', 'brazier', 'bread machine', 'broaster company', 'brown bobby', 'burjiko', 'butane torch', 'charbroiler', 'cheesemelter', 'chocolatera', 'coffee percolator', 'coffeemaker', 'comal (cookware)', 'combi steamer', 'cooker', 'list of cooking appliances', 'cooktop', 'corn roaster', 'crepe maker', 'deep fryer', 'electric cooker', 'field kitchen', 'fire pot', 'flattop grill', 'food steamer', 'footman (furniture)', 'fufu machine', 'halogen oven', 'haybox', 'horno', 'hot box (appliance)', 'hot plate', 'induction cooking', 'instant pot', 'kamado', 'kettle', 'kitchener range', 'krampouz', 'kujiejun', 'kyoto box', 'mess kit', 'multicooker', 'oven', 'pancake machine', 'pie iron', 'popcorn maker', 'pressure cooking', 'pressure frying', 'remoska', 'rice cooker', 'rice polisher', 'roasting jack', 'rocket mass heater', 'rollie eggmaster', 'rotisserie', 'sabbath mode', 'salamander broiler', 'samovar', 'shichirin', 'siru', 'slow cooker', 'solar cooker', 'soy milk maker', 'stove', 'susceptor', 'tandoor', 'thermal cooking', 'thermal immersion circulator', 'thermomix', 'toaster', 'trojan room coffee pot', 'turkey fryer', 'vacuum fryer', 'waffle iron', 'wet grinder', 'wet grinder (food)', 'whistling kettle', 'baking dish', 'baking tray', 'cake pan', 'can opener', 'chopping board', 'coffee press', 'colander', 'cooling rack', 'corkscrew', 'cutlery', 'dinnerware', 'eggbeater', 'egg slicer', 'electric mixer', 'fork', 'frying pan', 'garlic press', 'grater', 'glassware', 'grill pan', 'kitchen scissors', 'knives', 'mandolin', 'measuring cups and spoons', 'measuring spoon', 'meat slicer', 'mixing bowls', 'muffin tin', 'pasta server', 'peeler', 'pepper mill', 'pie dish', 'pizza stone', 'plates', 'potato masher', 'potato ricer', 'rolling pin', 'saucepan', 'serving fork', 'serving spoon', 'sheet pan', 'skillet', 'slotted spoon', 'soup spoon', 'spatula', 'spiral vegetable slicer', 'spoon', 'stock pot', 'steamers', 'strainer', 'timer', 'tomato slicer', 'tongs', 'tray', 'whisk', 'wok', 'wooden spoon']
two = ['beanpot', 'billycan', 'caquelon', 'casserole', 'cassole', 'cassolette', 'cast-iron cookware', 'cataplana', 'cauldron', 'cezve', 'chafing dish', 'chip pan', 'cousances', 'couscoussier', 'crepulja', 'crock (dishware)', 'dallah (coffee pot)', 'ding (vessel)', 'dolsot', 'dutch oven', 'earthenware', 'fermentation crock', 'fish kettle', 'food steamer', 'food warmer', 'french tian', 'frying pan', 'gamasot', 'grabit (cookware)', 'handi', 'instant pot', 'jebena', 'karahi', 'kazan (cookware)', 'marmite (cooking dish)', 'mold (cooking implement)', 'multicooker', 'olla', 'onggi', 'palayok', 'pipkin', 'porringer', 'potjiekos', 'pressure cooking', 'ramekin', 'rice cooker', 'roasting pan', 'sinseollo', 'siru', 'slow cooker', 'springform pan', 'stock pot', 'sufuria', 'tangia', 'tapayan', 'tava', 'terrine (cookware)', 'thermal cooking', 'ttukbaegi', 'uruli', 'wok', 'wonder pot']

for i in one:
    if i not in two:
        two.append(i)
        
print(two)


# In[26]:


one = ['beanpot', 'billycan', 'caquelon', 'casserole', 'cassole', 'cassolette', 'cast-iron cookware', 'cataplana', 'cauldron', 'cezve', 'chafing dish', 'chip pan', 'cousances', 'couscoussier', 'crepulja', 'crock (dishware)', 'dallah (coffee pot)', 'ding (vessel)', 'dolsot', 'dutch oven', 'earthenware', 'fermentation crock', 'fish kettle', 'food steamer', 'food warmer', 'french tian', 'frying pan', 'gamasot', 'grabit (cookware)', 'handi', 'instant pot', 'jebena', 'karahi', 'kazan (cookware)', 'marmite (cooking dish)', 'mold (cooking implement)', 'multicooker', 'olla', 'onggi', 'palayok', 'pipkin', 'porringer', 'potjiekos', 'pressure cooking', 'ramekin', 'rice cooker', 'roasting pan', 'sinseollo', 'siru', 'slow cooker', 'springform pan', 'stock pot', 'sufuria', 'tangia', 'tapayan', 'tava', 'terrine (cookware)', 'thermal cooking', 'ttukbaegi', 'uruli', 'wok', 'wonder pot', 'air fryer', 'auto reignition', 'bachelor griller', 'barbecue', 'barbecue grill', 'big green egg', 'brasero (heater)', 'brazier', 'bread machine', 'broaster company', 'brown bobby', 'burjiko', 'butane torch', 'charbroiler', 'cheesemelter', 'chocolatera', 'coffee percolator', 'coffeemaker', 'comal (cookware)', 'combi steamer', 'cooker', 'list of cooking appliances', 'cooktop', 'corn roaster', 'crepe maker', 'deep fryer', 'electric cooker', 'field kitchen', 'fire pot', 'flattop grill', 'footman (furniture)', 'fufu machine', 'halogen oven', 'haybox', 'horno', 'hot box (appliance)', 'hot plate', 'induction cooking', 'kamado', 'kettle', 'kitchener range', 'krampouz', 'kujiejun', 'kyoto box', 'mess kit', 'oven', 'pancake machine', 'pie iron', 'popcorn maker', 'pressure frying', 'remoska', 'rice polisher', 'roasting jack', 'rocket mass heater', 'rollie eggmaster', 'rotisserie', 'sabbath mode', 'salamander broiler', 'samovar', 'shichirin', 'solar cooker', 'soy milk maker', 'stove', 'susceptor', 'tandoor', 'thermal immersion circulator', 'thermomix', 'toaster', 'trojan room coffee pot', 'turkey fryer', 'vacuum fryer', 'waffle iron', 'wet grinder', 'wet grinder (food)', 'whistling kettle', 'baking dish', 'baking tray', 'cake pan', 'can opener', 'chopping board', 'coffee press', 'colander', 'cooling rack', 'corkscrew', 'cutlery', 'dinnerware', 'eggbeater', 'egg slicer', 'electric mixer', 'fork', 'garlic press', 'grater', 'glassware', 'grill pan', 'kitchen scissors', 'knives', 'mandolin', 'measuring cups and spoons', 'measuring spoon', 'meat slicer', 'mixing bowls', 'muffin tin', 'pasta server', 'peeler', 'pepper mill', 'pie dish', 'pizza stone', 'plates', 'potato masher', 'potato ricer', 'rolling pin', 'saucepan', 'serving fork', 'serving spoon', 'sheet pan', 'skillet', 'slotted spoon', 'soup spoon', 'spatula', 'spiral vegetable slicer', 'spoon', 'steamers', 'strainer', 'timer', 'tomato slicer', 'tongs', 'tray', 'whisk', 'wooden spoon']
one.sort()

sorted_one = []

for x in sorted(one):
    sorted_one.append(x)
    
print(sorted_one)
    


# In[50]:


f = open("CookingTechniques.txt", "r")

techniques = []
for tech in f:
    test = tech.split('\n')
    techniques.append(test[0].lower())
    
print(techniques)
        


# In[54]:


f = open("CookingTechniques.txt", "r")

techniques = []
for tech in f:
    test = tech.split(" - ")
    
for i in test:
    techniques.append(i.lower())

print(techniques)


# In[ ]:


one = ['acidulate', 'al dente', 'amandine', 'amylolytic process', 'anti-griddle', 'aspic', 'au gratin', 'au jus', 'au poivre', 'backwoods cooking', 'baghaar', 'bain-marie', 'baking', 'barding', 'barbecuing', 'baste', 'blanching', 'boiling', 'braising', 'brine', 'broasting', 'browning', 'candy making', 'caramelization', 'carry over cooking', 'casserole', 'charbroiling', 'cheesemaking', 'chiffonade', 'chinese cooking techniques', 'red cooking', 'velveting', 'clay pot cooking', 'coddling', 'concasse', 'conche', 'confit', 'cooking with alcohol', 'creaming', 'croquette', 'culinary triangle', 'curdling', 'cured fish', 'curing', 'deep frying', 'deglazing', 'degreasing', 'dough sheeting', 'dredging ', 'dry roasting', 'drying', 'dum pukht', 'dutch oven cooking', 'engastration', 'earth oven', 'egg wash', 'emulsify ', 'en papillote', 'en vessie', 'engastration', 'engine cooking', 'escagraph', 'fermentation', 'fillet', 'flambé', 'flattop grill', 'food preservation', 'canning', 'curing', 'home canning', 'fondue', 'fricassee', 'frost', 'frying', 'garnish', 'gentle frying', 'glazing', 'grating', 'grilling', 'hāngi', 'hibachi', 'high-altitude cooking', 'homogenization', 'hot salt frying', 'huff paste', 'indirect grilling', 'infusion', 'jugging', 'juicing', 'julienning', 'kalua', 'karaage', 'kho', 'kinpira', 'larding', 'low-temperature cooking', 'maceration', 'marination', 'meat cooking techniques', 'microwave cooking', 'mincing', 'mongolian barbecue', 'mother sauces', 'nappage', 'nixtamalization', 'one pot one shot (opos)', 'once-a-month cooking (oamc)', 'outdoor cooking', 'pan frying', 'parbaking', 'parboiling', 'pascalization', 'paste', 'pasteurization', 'flash pasteurization', 'pasteurized eggs', 'pellicle', 'pickling', 'pig roast', 'poaching', 'pre-ferment', 'pressure cooking', 'pressure frying', 'proofing', 'purée', 'reconstitution', 'reduction', 'rendering', 'ricing', 'rillettes', 'roasting', 'robatayaki', 'rotisserie', 'roux', 'sautéing', 'score', 'schwenker', 'searing', 'seasoning', 'separating eggs', 'shallow frying', 'shirred eggs', 'shrivelling', 'shuck', 'simmering', 'skimming', 'slow cooker', 'smoking', 'smothering', 'souring', 'sous-vide', 'spatchcock', 'spherification', 'steaming', 'food steamer', 'steeping', 'stewing', 'stir frying', 'straight dough', 'stuffing', 'sugar panning', 'sweating', 'swissing', 'syringe', 'tandoor', 'tataki', 'tempering', 'tempering (chocolate)', 'tempering (cooking)', 'tempering (spices)', 'tenderizing', 'thermal cooking', 'thermization', 'thickening', 'truss', 'turbo cooking', 'turkey fryer', 'vietnamese cooking techniques', 'whip', 'wok cooking', 'zest']
two = 


# In[3]:


ingredients = ["butter", "sliced green onions", "garlic, minced", "(10 ounce) package frozen chopped spinach , thawed, drained and squeezed dry", "ricotta cheese", "sour cream", "shredded Monterey Jack cheese", "(6 inch) corn tortillas", "(19 ounce) can enchilada sauce", "extra virgin olive oil", "(10 ounce) packages frozen chopped spinach", "onion, chopped", "dried oregano", "dried basil", "garlic, crushed", "(32 ounce) jar spaghetti sauce", "water", "non-fat cottage cheese", "(8 ounce) package part skim mozzarella cheese, shredded", "grated Parmesan cheese", "chopped fresh parsley", "salt", "black pepper", "egg", "lasagna noodles", "chopped fresh ginger", "garlic, chopped", "red curry paste", "(15 ounce) can coconut milk, divided", "(16 ounce) package chicken-style seitan, cut into strips or cubes", "smooth peanut butter", "white sugar", "vegetable oil", "tamari or soy sauce", "chili garlic sauce", "vegetarian oyster sauce", "sweet onion, chopped", "bunch fresh spinach, chopped", "green onions, chopped", "Yukon gold or red potato, cut into 1/4-inch slices", "vegetable broth", "salt", "shredded sharp Cheddar cheese, divided", "heavy cream", "garlic powder", "ground black pepper", "nutmeg", "pineapple juice", "banana, cut into chunks", "frozen strawberries", "frozen blueberries", "olive oil", "medium onion, chopped", "bay leaves", "ground cumin", "dried oregano", "salt", "stalks celery, chopped", "green bell peppers, chopped", "jalapeno peppers, chopped", "garlic, chopped", "(4 ounce) cans chopped green chile peppers, drained", "(12 ounce) packages vegetarian burger crumbles", "(28 ounce) cans whole peeled tomatoes, crushed", "chili powder", "ground black pepper", "(15 ounce) can kidney beans, drained", "(15 ounce) can garbanzo beans, drained", "(15 ounce) can black beans", "(15 ounce) can whole kernel corn", "potatoes, peeled and thinly sliced", "zucchini, thinly sliced", "red onions, thinly sliced", "ripe tomatoes, pureed", "olive oil", "chopped fresh parsley (optional)", "sea salt and freshly ground black pepper to taste", "eggplant, peeled and thinly sliced", "eggs, beaten", "Italian seasoned bread crumbs", "spaghetti sauce, divided", "(16 ounce) package mozzarella cheese, shredded and divided", "grated Parmesan cheese, divided", "dried basil", "zucchini, finely grated", "salt", "Batter:", "egg", "all-purpose flour", "Parmesan cheese", "salt", "ground black pepper to taste", "oil for frying", "Toppings:", "grated Parmesan cheese, or to taste", "salt", "sour cream, for topping", "whole fresh mushrooms", "vegetable oil", "minced garlic", "(8 ounce) package cream cheese, softened", "grated Parmesan cheese", "ground black pepper", "onion powder", "ground cayenne pepper", "quinoa", "water", "extra-virgin olive oil", "limes, juiced", "ground cumin", "salt", "red pepper flakes, or more to taste", "halved cherry tomatoes", "(15 ounce) can black beans, drained and rinsed", "green onions, finely chopped", "chopped fresh cilantro", "salt and ground black pepper to taste", "heads broccoli, separated into florets", "extra-virgin olive oil", "sea salt", "ground black pepper", "garlic, minced", "lemon juice", "potatoes, peeled and cubed", "vegetable oil", "yellow onion, diced", "garlic, minced", "ground cumin", "cayenne pepper", "curry powder", "garam masala", "(1 inch) piece fresh ginger root, peeled and minced", "salt", "(14.5 ounce) can diced tomatoes", "(15 ounce) can garbanzo beans (chickpeas), rinsed and drained", "(15 ounce) can peas, drained", "(14 ounce) can coconut milk", "Smoothie:", "frozen blueberries", "banana", "water", "cashew butter", "vanilla extract", "Toppings:", "banana, sliced", "sliced almonds", "unsweetened shredded coconut", "olive oil", "onion, diced", "sliced fresh mushrooms", "salt, or more to taste", "diced red bell pepper", "jalapeno pepper, seeded and sliced", "cumin", "paprika", "ground turmeric", "freshly ground black pepper, plus more to taste", "cayenne pepper", "(28 ounce) can crushed San Marzano tomatoes, or other high-quality plum tomatoes", "water, or more as needed", "eggs", "crumbled feta cheese", "chopped fresh parsley", "(12 inch) pre-baked pizza crust", "pesto", "ripe tomato, chopped", "green bell pepper, chopped", "(2 ounce) can chopped black olives, drained", "red onion, chopped", "(4 ounce) can artichoke hearts, drained and sliced", "crumbled feta cheese", "ricotta cheese", "chopped spinach", "egg, lightly beaten", "ground black pepper", "basil leaves, torn", "extra-virgin olive oil, or more to taste", "garlic (optional)", "pine nuts", "extra large zucchini", "toothpicks, soaked in water", "pasta sauce", "grated Parmigiano-Reggiano cheese", "Harissa Sauce:", "roasted red pepper, peeled and minced", "chopped shallot", "minced garlic", "olive oil", "chopped fresh mint", "lime juice", "Dijon mustard", "minced fresh cilantro", "salt", "red pepper flakes", "ground coriander", "ground black pepper", "cayenne pepper", "Mashed Beans:", "canned cannellini beans", "water, or as needed", "truffle oil", "salt", "ground black pepper", "Portobello Mushrooms:", "portobello mushroom caps", "olive oil", "vegetable broth", "salt", "ground black pepper", "butter", "olive oil", "mushrooms, sliced", "shallots, chopped", "cherry tomatoes, halved", "heavy whipping cream", "zucchini, cut into noodle-shape strands", "chopped fresh basil", "salt and ground black pepper to taste", "(8 ounce) package dried rice noodles", "olive oil", "head romaine lettuce, chopped", "red bell pepper, diced", "chopped red onion", "green onions, chopped", "cucumber, diced", "chopped fresh basil, or to taste", "chopped fresh cilantro, or to taste", "(1 inch) piece fresh ginger root, minced", "jalapeno pepper, seeded and minced", "garlic, minced", "Sauce:", "olive oil", "rice vinegar", "soy sauce", "white sugar", "lemon, juiced", "lime, juiced", "salt", "ground turmeric", "paprika", "Vegan Green Chile Cilantro Sauce:", "unsalted raw cashews", "(4 ounce) can chopped green chile peppers", "hemp milk", "jalapeno pepper with seeds, or more to taste", "salt", "chopped fresh cilantro", "water", "quinoa", "romaine hearts, chopped", "(15 ounce) cans black beans, rinsed and drained", "chopped red bell pepper", "chopped red onion", "vocados, chopped", "vocados - peeled, pitted, and mashed", "lime, juiced", "salt", "diced onion", "chopped fresh cilantro", "roma (plum) tomatoes, diced", "minced garlic", "ground cayenne pepper (optional)", "vegetable oil", "onion, chopped", "garlic, chopped", "quinoa", "vegetable broth", "ground cumin", "cayenne pepper", "salt and ground black pepper to taste", "frozen corn kernels", "(15 ounce) cans black beans, rinsed and drained", "chopped fresh cilantro", "butter", "(8 ounce) package cream cheese", "garlic powder", "milk", "grated Parmesan cheese", "ground black pepper", "kiwis, peeled and diced", "Golden Delicious apples - peeled, cored and diced", "raspberries", "strawberries", "white sugar", "brown sugar", "fruit preserves, any flavor", "(10 inch) flour tortillas", "butter flavored cooking spray", "cinnamon sugar", "butter", "almonds, blanched and slivered", "spinach, rinsed and torn into bite-size pieces", "dried cranberries", "toasted sesame seeds", "poppy seeds", "white sugar", "minced onion", "paprika", "white wine vinegar", "cider vinegar", "vegetable oil", "Brussels sprouts, ends trimmed and yellow leaves removed", "olive oil", "kosher salt", "freshly ground black pepper", "butter", "heavy cream", "garlic, crushed", "freshly grated Parmesan cheese", "chopped fresh parsley", "sweet potato, cubed", "white sugar", "eggs, beaten", "salt", "butter, softened", "milk", "vanilla extract", "packed brown sugar", "all-purpose flour", "butter, softened", "chopped pecans", "(16 ounce) can black beans, drained and rinsed", "green bell pepper, cut into 2 inch pieces", "onion, cut into wedges", "garlic, peeled", "egg", "chili powder", "cumin", "Thai chili sauce or hot sauce", "bread crumbs", "(8 ounce) package elbow macaroni", "(8 ounce) package shredded sharp Cheddar cheese", "(12 ounce) container small curd cottage cheese", "(8 ounce) container sour cream", "grated Parmesan cheese", "salt and pepper to taste", "dry bread crumbs", "butter, melted", "roma (plum) tomatoes, chopped", "sun-dried tomatoes, packed in oil", "minced garlic", "olive oil", "balsamic vinegar", "fresh basil, stems removed", "salt", "ground black pepper", "French baguette", "shredded mozzarella cheese", "minced garlic", "olive oil", "head cauliflower, separated into florets", "grated Parmesan cheese", "salt and black pepper to taste", "chopped fresh parsley", "vegetable oil", "onion, chopped", "(10 ounce) package frozen chopped spinach, thawed and drained", "eggs, beaten", "shredded Muenster cheese", "salt", "ground black pepper", "garlic", "(10 ounce) package frozen chopped spinach, thawed and drained", "(14 ounce) can artichoke hearts, drained and chopped", "(10 ounce) container Alfredo-style pasta sauce", "shredded mozzarella cheese", "grated Parmesan cheese", "(8 ounce) package cream cheese, softened", "(8 ounce) package cream cheese, softened", "mayonnaise", "grated Parmesan cheese", "grated Romano cheese", "garlic, peeled and minced", "dried basil", "garlic salt", "salt and pepper to taste", "(14 ounce) can artichoke hearts, drained and chopped", "frozen chopped spinach, thawed and drained", "shredded mozzarella cheese", "onion, chopped", "olive oil", "carrots, diced", "stalks celery, chopped", "garlic, minced", "dried oregano", "bay leaf", "dried basil", "(14.5 ounce) can crushed tomatoes", "dry lentils", "water", "spinach, rinsed and thinly sliced", "vinegar", "salt to taste", "ground black pepper to taste", "vegetable oil", "onion, chopped", "garlic, minced", "canned kidney beans, drained", "water", "chili powder", "prepared mustard", "ground cumin", "cayenne pepper, or to taste", "soy sauce", "mashed cooked sweet potatoes", "(10 inch) flour tortillas, warmed", "shredded Cheddar cheese", "cranberries", "white sugar", "orange juice"]

ingredientsKB = {}

ingredientsKB['dairyIngredients'] = ['buttermilk', 'cottage', 'cream', 'creamer', 'creamy', 'creme', 'ghee', 'half-and-half', 'milk', 'yogurt']
ingredientsKB['cheeses'] = ['bocconcini', 'mozzarella', 'gouda', 'swiss', 'brie']
ingredientsKB['meats'] = ['bacon', 'beefs', 'burgers', 'chorizo', 'dogs', 'frankfurters', 'giblets', 'ham', 'lambs', 'livers', 'meatballs', 'meatloaves', 'meats', 'mignon', 'mincemeat', 'pepperonis', "pig's", 'porks', 'prosciutto', 'ribs', 'roasts', 'sausages', 'sirloin', 'tripe', 'veal', 'venison', 'kielbasas', 'liverwurst', 'wieners', 'cotechino', 'linguica', 'pastrami', 'squirrels', 'sauerbraten', 'picadillo', 'carcass', 'brains', 'mortadella', 'rounds', 'sweetbread', 'toad', 'tinga', 'embutido', 'hash', 'broil', 'brisket', 'franks', 'pigs', 'rouladen', 'chops', 'scrapple', 'barbeque', 'spareribs']
ingredientsKB['poultry'] = ['bologna', 'bratwursts', 'chickens', 'ducks', 'goose', 'hens', 'pollo', 'salami', 'turkey', 'pheasant', 'quail', 'turducken', 'drumettes', 'wings', 'roosters']
ingredientsKB['fish'] = ['albacores', 'bass', 'catfish', 'cods', 'fish', 'flounder', 'grouper', 'haddock', 'halibut', 'mahi', 'monkfish', 'salmon', 'shark', 'snapper', 'sole', 'swordfishes', 'trouts', 'tunas', 'bluefish', 'bonito', 'rockfish', 'mackerel', 'naruto', 'drum', 'marlin', 'tilapia', 'carp', 'kingfish', 'mullets', 'whitefish', 'kippers', 'torsk', 'saltfish']
ingredientsKB['seafoods'] = ['anchovies', 'calamaris', 'clams', 'crabs', 'crabmeat', 'crawfish', 'lobsters', 'mussels', 'oysters', 'prawns', 'scallops', 'seafood', 'shrimps', 'squids', 'snails', 'shellfish', 'caviar']
ingredientsKB['mainProteins'] = ['beans', 'chickpeas', 'nuts', 'seeds', 'tofu', 'whey', 'buckwheat', 'protein', 'soybeans', 'soy', 'tempeh', 'lentils', 'masoor', 'gluten', 'pine', 'falafel', 'portobello']
ingredientsKB['fruits'] = ['apples', 'apricots', 'bananas', 'blackberries', 'blueberries', 'cantaloupe', 'cherries', 'citrons', 'citrus', 'coconuts', 'cranberries', 'currants', 'elderberries', 'figs', 'fruitcakes', 'fruits', 'gooseberries', 'grapefruit', 'grapes', 'guava', 'honeydew', 'huckleberries', 'kiwis','kumquats', 'lemonade', 'lemons', 'limes', 'mangoes', 'marrons', 'mincemeat', 'mulberries', 'nectarines', 'oranges', 'papayas', 'peaches', 'pears', 'persimmon', 'persimmons', 'pineapples', 'plums', 'prunes', 'raisins',  'raspberries', 'slushies', 'smoothies', 'sorrel', 'strawberries', 'tangerines', 'watermelons', 'yuzu', 'lingonberries', 'plantains', 'juniper', 'lingonberries', 'pomegranates', 'serviceberries', 'zinfandel', 'lychees', 'carambola', 'uvas']
ingredientsKB['vegetables'] = ['artichokes', 'arugula', 'asparagus', 'avocados', 'bamboo', 'beets', 'broccoli', 'cabbage', 'calzones', 'carrots', 'cauliflower', 'celery', 'chilis', 'chives', 'choy', 'cilantro', 'coleslaw', 'coriander', 'cucumber', 'cucumbers', 'dates', 'eggplant', 'eggplants', 'endive', 'escarole', 'galangal', 'haystacks', 'jicama', 'kale', 'kohlrabi', 'kucai', 'leeks', 'lettuce', 'mushrooms', 'okra', 'olives', 'onions', 'parsley', 'parsnips', 'peas', 'peppers', 'pickles', 'pizzas', 'potatoes', 'pumpkins', 'radishes', 'rutabagas', 'salad', 'sauerkraut', 'shallots', 'slaws', 'spinach', 'sprouts', 'squash', 'tamarind', 'taros', 'tomatillo', 'tomatillos', 'tomatoes', 'turnips', 'vegetable', 'vegetables', 'veggies', 'watercress', 'yams', 'zucchinis', 'chervil', 'daikon', 'iceberg', 'nopales', 'pimentos', 'radicchio', 'karengo', 'nori', 'succotash', 'truffle', 'chard', 'fries', 'leaves', 'browns', 'romain', 'palm', 'sorghum', 'aloo', 'haricots', 'caprese', 'salata', 'shiitake']
ingredientsKB['sugars'] = ['Jell-O®', 'butterscotch', 'candied', 'candy', 'caramels', 'frosting', 'fructose', 'gingersnaps', 'glaces', 'glaze', 'glycerin', 'glycerol', 'gumdrops', 'gummi', 'honey', 'icing', 'jellybeans', 'ladyfingers', 'licorice', 'macaroons', 'maple', 'marrons glaces', 'marshmallows', 'marzipan', 'molasses', 'pastries', 'pectin', 'peppermints', 'pie', 'piping', 'puddings', 'puff', 'sourball', 'sprinkles', 'sucanat', 'sugar', 'sweetener', 'syrup', 'tarts', 'toffee', 'twinkies', 'colaciones', 'sherbet', "hershey®'s", 'candies', "confectioners'", 'fudge', 'taffy', 'pink', 'sherbet']
ingredientsKB['sauces'] = ['alfredo', 'applesauce', 'chutney', 'cannoli', 'dips', 'guacamole', 'hummus', 'paste', 'spreads', 'tahini', 'tzatziki', 'denjang', 'salsa', 'sauce', 'tapenade', 'coating', 'teriyaki', 'aioli', 'checca', 'amatriciana', 'ragu', 'marinara']
ingredientsKB['condiments'] = ['dressing', 'jam', 'ketchup', 'marinade', 'marjoram', 'mayonnaise', 'mirin', 'mustard', 'pesto', 'relish', 'shoyu', 'tamari', 'vinaigrette', 'gochujang']
ingredientsKB['soups'] = ['broth', 'chowder', 'dashi', 'soup', 'stew', 'jambalaya', 'gumbo', 'gazpacho', 'goulash', 'pho', 'slumgullion', 'cioppino', 'minestrone']
ingredientsKB['nuts'] = ['almonds', 'butternuts', 'candlenuts', 'cashews', 'chestnuts', 'hazelnuts', 'macadamia', 'nuts', 'peanuts', 'pecans', 'pistachios', 'walnuts', 'nuts']
ingredientsKB['alcoholicIngredients'] = ['anisette', 'beer', 'bitters', 'bourbon', 'brandy', 'cacao', 'chambord', 'champagne', 'cognac', 'eggnog', 'kirsch', 'kirschwasser', 'liqueur', 'rum', 'schnapps', 'sherry', 'ale', 'spritz', 'tequila', 'vermouth', 'vodka', 'whiskey', 'wine', 'campari', 'alcohol', 'absinthe', 'cachaca', 'liquor', 'cointreau', 'curacao', 'sake', 'sec', 'calvados', 'galliano', 'lillet', 'margaritas', 'coladas', 'negroni', 'mojitos', 'mimosas', 'bahama', 'slammer', 'sauvignon', 'chablis', 'martinis', 'tequinis', 'spritzs', 'cosmopolitan', 'hurricanes', 'sangria', 'sex', "shaggy's", 'nipples', 'stoli']
ingredientsKB['spices'] = ['allspice', 'anise', 'arrowroot', 'basil', 'bay', 'capers', 'caraway', 'cardamom', 'cassava', 'cayenne', 'chocolate', 'cilantro', 'cinnamon', 'cloves', 'cocoa', 'coriander', 'cumin', 'dill', 'fennel', 'flax', 'garlic', 'ginger', 'herbs', 'kalonji', 'mace', 'masala', 'miso', 'monosodium', 'nutmeg', 'oregano', 'paprika', 'pepper', 'peppercorns', 'pimento', 'poppy', 'poppyseed', 'powder','rhubarb', 'rosemary', 'saffron', 'sage', 'salt', 'savory', 'seasoning', 'sesame', 'spices', 'sunflower', 'tarragon', 'thyme', 'turmeric', 'vanilla', 'watercress', 'spearmint', 'comfort']
ingredientsKB['spicy'] = ['angelica', 'dijon', 'horseradish', 'jerk', 'wasabi', 'spicy']
ingredientsKB['hotPeppers'] = ['jalapenos', 'pepperoncinis', 'chiles']
ingredientsKB['grains'] = ['bagels', 'baguettes', 'barley', 'biscuits', 'bran', 'bread', 'buns', 'cereal', 'corn', 'cornbread', 'cornstarch', 'couscous', 'crackers', 'croutons', 'crusts', 'dough', 'granola', 'hominy', 'kasha', 'masa', 'matzo', 'millet', 'muffins', 'oats', 'pitas', 'popcorn', 'pretzels', 'quinoa', 'rice', 'rolls',  'shortbread', 'sourdough', 'stuffing', 'tapioca', 'toasts', 'tortillas', 'wheat', 'kaiser', 'cornmeal', 'breadcrumbs', 'graham', 'bulgur', 'farina', 'oatmeal', 'croissants', 'polenta', 'grits', 'pumpernickel', 'sago', 'seitan', 'grains', 'taters', 'risotto', 'shells', 'amarettini', 'mochi', 'cornflakes', 'pilaf', 'puppies']
ingredientsKB['pastas'] = ['farfalle', 'fettuccine', 'lasagnas', 'linguine', 'mac', 'macaroni', 'manicotti', 'noodles', 'pasta', 'farfel', 'vermicelli', 'tagliatelle', 'cannelloni', 'penne']
ingredientsKB['wrappedMeals'] = ['burritos', 'calzones', 'dumplings', 'empanadas', 'fajitas', 'hero', 'pie', 'pinwheels', 'pizzas', 'quesadillas', 'sandwiches', 'tacos', 'tourtiere', 'wontons', 'hoagie', 'pierogies', 'rarebit', 'joes', 'enchiladas', 'pierogi', 'bierrocks', 'torta', 'reuben', 'wraps', 'piroshki', 'tamales', 'bruschetta', 'antipasto', 'hamburger', 'muffuletta', 'blanket', 'runzas', 'samosas', 'sambousas', 'chalupas', 'spanakopita', 'submarine']
ingredientsKB['pastaDishes'] = ['casseroles', 'curry', 'lasagna', 'marzetti', 'mostaccioli', 'spaghetti', 'stroganoff', 'ziti', 'pastini', 'pastitsio', 'fideo', 'spaghettini', 'moussaka', 'tortellinis', 'tallerine', 'talerine', 'scampi', 'ravioli', 'pad', 'gnocchi', 'spaetzle', 'stromboli']
ingredientsKB['vegetableDishes'] = ['tabbouleh', 'kabobs', 'suey', 'frittatas', 'quiches', 'raita', 'shieldzini', 'stir', 'sukiyaki']
ingredientsKB['drinks'] = ['beverage', 'cider', 'coffee', 'dew™', 'drink', 'eggnog', 'epazote', 'espresso', 'gin', 'juices', 'lemonade', 'limeade', 'milk', 'rosewater', 'soda', 'tea', 'wassail', 'punch', 'shake', 'shirley', 'americano']
ingredientsKB['cookingLiquids'] = ['oil', 'vinegar', 'water', 'snow', 'ice']
ingredientsKB['bakingIngredients'] = ['ammonia', 'baking', 'eggs', 'flour', 'margarine', 'yeast', 'bisquick®']
ingredientsKB['cookingFats'] = ['butter', 'gelatin', 'gravy', 'lard', 'lecithin', 'ovalette', 'shortening', 'xanthan', 'suet']
ingredientsKB['extras'] = ['carnations', 'coloring', 'dust', 'flowers', 'lilies', 'spray', 'toppings', 'drippings', 'powdered', 'gold']
ingredientsKB['fasteners'] = ['sticks', 'skewers', 'toothpicks']
ingredientsKB['adhesives'] = ['glue']
ingredientsKB['containers'] = ['jars']
ingredientsKB['flavorings'] = ['extract', 'flavorings', 'mint', 'pandan', 'hickory', 'flavored', 'mesquite', 'wood', 'hardwood']
ingredientsKB['mixtures'] = ['food', 'mixes']

# words with succeeding noun ("milk" or "cake")
ingredientsKB['nonDairyMilks'] = ['almond', 'soy', 'coconut']
ingredientsKB['cakeTypes'] = ['pound', 'sponge', 'white', 'yellow', 'bunny', "'scratch'"]



# In[38]:


import nltk
import re

all_grams = set()

for n in ingredients:
    n = n.lower()
    n = n.replace("(", "")
    n = n.replace(")", "")
    gram = list(nltk.everygrams(n.split()))
    
    for g in gram:
        if len(g) > 1:
            all_grams.add(' '.join(g))
        else:
            all_grams.add(g[0])

        


# In[36]:


foodPoints = {}

for category in ingredientsKB.keys():
    for food in ingredientsKB[category]:
        if food in all_grams:
            if food not in foodPoints:
                foodPoints[food] = 1
            else:
                foodPoints[food] += 1
                
print(foodPoints)


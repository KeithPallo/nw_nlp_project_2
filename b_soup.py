
# running python version 3.6

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

print(test_directions)




from ing_parser import parse
import json
from pprint import pprint

# import nltk
# from nltk import *

print(parse('2 liters of milk'))
print(parse('2 lbs milk'))
print(parse('1 lbs milk'))
print(parse('1 lb milk'))
print(parse('1 pound milk'))
print(parse('1 # milk'))
print(parse('1 t milk.'))
print(parse('1 T milk.'))
print(parse('thirteen T milk'))
print("")
print(parse("1 bunch celery, cleaned and cut into 4 inch pieces"))
print("")
print(parse("4 teaspoons of Keith"))
print("")
print("")
print(parse("2 (8 ounce) packages cream cheese, softened"))
print(parse("2 8 ounce packages cream cheese, softened"))
print(parse("1 1/2 cups shredded Cheddar cheese"))
print(parse("1 cups shredded Cheddar cheese"))

print(parse("1 pound skinless, boneless chicken breast halves - cubed"))
# error
print(parse("1 cup sliced carrotsprint"))
print(parse("1 cup frozen green peas"))
print(parse("1/2 cup sliced celery"))

print(parse("1/3 cup butter"))
print(parse("1/3 cup chopped onion"))
print(parse("1/3 cup all-purpose flour"))
print(parse("1/2 teaspoon salt"))
print(parse("1/4 teaspoon black pepper"))
print(parse("1/4 teaspoon celery seed"))
print(parse("1 3/4 cups chicken broth"))
print(parse("2/3 cup milk"))
print(parse("2 (9 inch) unbaked pie crusts"))
print(parse("2 9 inch unbaked pie crusts"))
print(parse(".9 inch unbaked pie crusts"))
print(parse("0.9 inch unbaked pie crusts"))

print(parse("6 frozen skinless, boneless chicken breast halves"))
print(parse("1 gal. of peanuts"))
print(parse("salt and ground black pepper to taste"))
print(parse("1 (10.75 ounce) can condensed Cheddar cheese soup"))
print(parse("1 10.75 ounce can condensed Cheddar cheese soup"))
print(parse("1/2 cup butter"))
print(parse("200 cans of condensed Cheddar cheese soup"))

print(parse("2 gallons of peanuts"))
print(parse("2 1/2 gallons of peanuts"))
print(parse("2 5 gallons of peanuts"))
print(parse("2 (9 inch) unbaked pie crusts"))
print(parse("6 slices ham"))




# s1 = '2 liters of milk'
# s2 = '2 lbs milk'
# s3 = '1 lbs milk'
# s4 = '1 lb milk'
# s5 = '1 pound milk'
# s6 = '1 # milk'
# s7 = '1 t milk.'
# s8 = '1 T milk.'
# s9 = 'thirteen T milk'
# s10 = "1 bunch celery, cleaned and cut into 4 inch pieces"
# s11 = "4 teaspoons of Keith"
# s12 = "2 (8 ounce) packaged cream cheese, softened"
# s13 = "2 8 ounce packaged cream cheese, softened"
# s14 = "1 1/2 cups shredded Cheddar cheese"
# s15 = "1 cups shredded Cheddar cheese"
#
# s16 = "1 pound skinless, boneless chicken breast halves - cubed"
# # error
# s17 = "1 cup sliced carrotsprint"
# s18 = "1 cup frozen green peas"
# s19 = "1/2 cup sliced celery"
#
# s20 = "1 onion minced blah"
# s21 = "1/3 cup chopped onion"
# s22 = "1/3 cup all-purpose flour"
# s23 = "1/2 teaspoon salt"
# s24 = "1/4 teaspoon black pepper"
# s25 = "1/4 teaspoon celery seed"
# s26 = "1 3/4 cups chicken broth"
# s27 = "2/3 cup milk"
# s28 = "2 (9 inch) unbaked pie crusts"
# s29 = "2 9 inch unbaked pie crusts"
# s30 = ".9 inch unbaked pie crusts"
# s31 = "0.9 inch unbaked pie crusts"
#
# s32 = "6 frozen skinless, boneless chicken breast halves"
# s33 = "1 gal. of peanuts"
# s34 = "salt and ground black pepper to taste"
# s35 = "1 (10.75 ounce) can condensed Cheddar cheese soup"
# s36 = "1 10.75 ounce can condensed Cheddar cheese soup"
# s37 = "1/2 cup butter"
# s38 = "200 cans of condensed Cheddar cheese soup"
#
# s39 = "2 1/2 gallons of peanuts"
# s40 = "2 (9 inch) unbaked pie crusts"
#
# s0 = []
#
# s0.extend((
# 		  s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24,
# 		  s25, s26, s27, s28, s29, s30, s31, s32, s33,
# 		  s34, s35, s36, s37, s38, s39, s40))
#
# for each in s0:
# 	t = word_tokenize(each)
# 	x = nltk.pos_tag(t)
# 	# print(s0)
# 	# print(t)
# 	# print(x)
# 	for each in x:
# 		if 'VB' in each[1]:
# 			print(each[0])
#
# with open('quantity_kb.json') as f:
# 	quantity = json.load(f)
# print(quantity)
#
# if 'thirty' in quantity.values():
# 	print(True)
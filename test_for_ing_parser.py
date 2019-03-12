from ing_parser import parse
import json
from pprint import pprint

# import nltk
# from nltk import *

print(parse("1 pinch paprika, or as desired (optional)"))
print(parse("1 (10.75 ounce) can condensed Cheddar cheese soup (such as Campbell's®)"))
print(parse("2 cups whole milk"))
print(parse("2 eggs, well beaten"))
print(parse("1 (16 ounce) package shredded Cheddar cheese, divided"))
print(parse("juice the strawberries"))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))
# print(parse(""))




# s1 = 'finely'
# s2 = 'fresh'
# s3 = 'extra-virgin'
# s4 = 'tasty'
# s5 = 'broken'
# s6 = 'sweat'
# s7 = 'sweated'
# s8 = 'toasted'
# s9 = 'roast'
# s10 = 'roasted'
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
# 	# print(t)
# 	print(x)
# 	# for each in x:
# 	# 	if 'RB' in each[1]:
# 	# 		print(each[0])

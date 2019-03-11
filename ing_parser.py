import re
import json
from pprint import pprint

#with open('ingredients_kb.json') as f:
#	ingredients = json.load(f)

with open('quantity_kb.json') as f:
	quantity = json.load(f)

with open('measurements_kb.json') as f:
	measurements = json.load(f)

# tools kb could go here

#ing_list = []
#for each in ingredients:
#	ing_list.extend(ingredients[each])

qty_list = []
for each in quantity:
	qty_list.extend(quantity[each])

measurement_list = []
for each in measurements:
	measurement_list.extend(measurements[each])

# print(measurement_list[1])

ingredient_string = re.compile(
	# Groups:
	# 1 = All #s quantity that's not in parentheses
	# 2 = Whole # of Group 1
	# 3/4 = Second whole # or full fraction
	# 5/6 = Measurements
	# 7/8 = n/a of Measurements
	# 9/10 = Name

	# 1, 2, 3/4
	# Note: ? required at end so '2' in '2 (8 ounce)' doesn't become '2 (8'
	r'(([(0-9).][\d.\s])?'
	r'(\s?(%s)\s*)*)'
	# 5/6
	r'(\s?(%s)\s+)?'
	# 7/8
	r'(\s?(%s)\s+)?'
	# 9/10
	r'(\s?(.+))?'
	% ('|'.join(qty_list),
	   '|'.join(measurement_list),
	   '|'.join(["of", "off"])))


# ingredient_string = re.compile(
# 	r'(?P<quantity>([\d\.,][\d\.,\s/]*)?[\r\n\t\f\v ]*((%s)[\r\n\t\f\v ]*)*)?([\r\n\t\f\v ]*(?P<unit>%s)[\r\n\t\f\v ]+)?([\r\n\t\f\v ]*(%s)[\r\n\t\f\v ]+)?([\r\n\t\f\v ]*(?P<name>.+))?' % (
# 	'|'.join(NUMBERS), '|'.join(b), '|'.join(PREPOSITIONS)))

# descriptor = if not in ingredients kb, adjective?
# preparation = verb phrase

def parse(string):
	reg = ingredient_string.match(string)

	# in name: has (??) at front & measurement == '', measurement = (??)
	# in name: if phrase in ing_list, return it, else return the whole name
	# in name: parse descriptors as ??
	# in name: parse preparation as verb phrase??
	n = {'name': (reg.group(9) or '').strip().lower()}
	# in quantity: check w/ miriam & jason
	# if second # in quantity is an integer (whole #), keep that in name
	spl = reg.group(1).split(' ')
	if spl[0] == spl[-1]:
		q = {'quantity': (reg.group(1) or '').strip().lower()}
	elif spl[0] != spl[-1]:
		if '/' in spl[-1]:
			q = {'quantity': (reg.group(1) or '').strip().lower()}
		else:
			q = {'quantity': (spl[0] or '').strip().lower()}
			m = {}
	# in measurement: if name has (something) at front & measurement == '', measurement = (something) without paren
	m = {'measurement': (reg.group(6) or '').strip()}
	parsed = {**q, **n, **m}
	# print(reg.group(1))
	# print(reg.group(1))
	# print(reg.group(1))
	return parsed

# return {**n}
# return {**q}
# return {**m}

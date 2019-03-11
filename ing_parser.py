import re
import json

<<<<<<< HEAD
#with open('ingredients_kb.json') as f:
#	ingredients = json.load(f)
=======
# Load in associated bd's

# with open('ingredients_kb.json') as f:
# 	ingredients = json.load(f)
>>>>>>> dc614cb507be68dc2aa758d7fd80828307d18a7a

with open('quantity_kb.json') as f:
	quantity = json.load(f)

with open('measurements_kb.json') as f:
	measurements = json.load(f)

# ingredients_list = []
# for each in ingredients:
# 	ingredients_list.extend(ingredients[each])

<<<<<<< HEAD
#ing_list = []
#for each in ingredients:
#	ing_list.extend(ingredients[each])
=======
# Make simple lists for quantity and measurement
>>>>>>> dc614cb507be68dc2aa758d7fd80828307d18a7a

qty_list = []
for each in quantity:
	qty_list.extend(quantity[each])

measurement_list = []
for each in measurements:
	measurement_list.extend(measurements[each])

# Create regex pattern

ingredient_string = re.compile(
	# Groups may have changed, but originally were:
	# 0 = Whole string
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


def parse(string):
	reg = ingredient_string.match(string)

	n = {'name': (reg.group(9) or '').strip().lower()}
	q = {'quantity': (reg.group(1) or '').strip().lower()}
	m = {'measure': (reg.group(6) or '').strip()}

	# yet to do:
	# if in name: if phrase in ingredients_list, return it, else return the whole name
	# if in name: parse preparation as verb phrase
	# if in name: parse descriptors as all else

	# looks for parentheses in name
	if '(' in reg.group(9) and ')' in reg.group(9):
		mesPar = re.findall(r'(\(.*?\))', reg.group(9))
		mesWO = mesPar[0][1:-1]
		split2 = mesWO.split()
		for each in split2:
			if each in measurement_list:
				remove_mes_from_name = reg.group(9).replace(mesPar[0], '')
				n = {'name': (remove_mes_from_name or '').strip().lower()}
				m = {'measure': (split2[0] + ' ' + split2[-1] or '').strip()}

	# if second # in quantity is a whole #, add it to measurement
	if reg.group(1) != '':
		splitQ = reg.group(1).split()
		if splitQ[-1] == '':
			splitQ = splitQ[0:-1]
		if splitQ[0] == splitQ[-1]:
			q = {'quantity': (reg.group(1) or '').strip().title()}
		else:
			if '/' in str(splitQ[-1]):
				q = {'quantity': (reg.group(1) or '').strip().title()}
			else:
				q = {'quantity': (splitQ[0] or '').strip().title()}
				m = {'measure': (splitQ[-1] + ' ' + str(reg.group(6)) or '').strip()}

	# If statement for measurement
	if m == {'measure': ''} or 'None' in m['measure'] and r'\d' not in m['measure']:
		splitN = reg.group(9).split()
		for each in splitN:
			if each in measurement_list:
				m = {'measure': str(each)}

	# If statement for quantity
	if q == {'quantity': ''}:
		q = {'quantity': 'n/a'}
	parsed = {**q, **n, **m}

	return parsed

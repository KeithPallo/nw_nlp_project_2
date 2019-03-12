import re
import json
import nltk
from nltk import *

# with open('ingredients_kb.json') as f:
# 	ingredients = json.load(f)

with open('quantity_kb.json') as f:
	quantity = json.load(f)

with open('measurements_kb.json') as f:
	measurements = json.load(f)

with open('preparations_kb.json') as f:
	preparations = json.load(f)

with open('descriptors_kb.json') as f:
	descriptors = json.load(f)

# ingredients_list = []
# for each in ingredients:
# 	ingredients_list.extend(ingredients[each])

qty_list = []
for each in quantity:
	qty_list.extend(quantity[each])

measurement_list = []
for each in measurements:
	measurement_list.extend(measurements[each])

preparations_list = []
for each in preparations:
	preparations_list.extend(preparations[each])

descriptors_list = []
for each in descriptors:
	descriptors_list.extend(descriptors[each])

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
	   '|'.join(["of", "off", "to"])))


def parse(string):
	reg = ingredient_string.match(string)

	n = {'name': (reg.group(9) or '').strip().lower()}
	q = {'quantity': (reg.group(1) or '').strip().lower()}
	m = {'measurement': (reg.group(6) or '').strip()}
	p = {'preparation': ''}
	d = {'descriptor': ''}

	# yet to do:
	# if in name: if phrase in ingredients_list, return it, else return the whole name
	# if in name: parse preparation as verb phrase AND then use preparation KB
	# if in name: parse descriptors as all else

	# create bigrams from name
	splitNcopy = reg.group(9).split()
	spliteach = []
	bgrams = []
	for each in splitNcopy:
		each = each.replace(',', '')
		each = each.replace('(', '')
		each = each.replace(')', '')
		spliteach.append(each)
		bgrams += list(nltk.bigrams(spliteach))

	# looks for parentheses in name
	if '(' in reg.group(9) and ')' in reg.group(9):
		mesPar = re.findall(r'(\(.*?\))', reg.group(9))
		mesWO = mesPar[0][1:-1]
		split2 = mesWO.split()
		for each in split2:
			if each in measurement_list:
				remove_mes_from_name = reg.group(9).replace(mesPar[0], '')
				remove_mes_from_name = remove_mes_from_name.replace('  ', ' ')
				n = {'name': (remove_mes_from_name or '').strip().lower()}
				m = {'measurement': (split2[0] + ' ' + split2[-1] or '').strip()}

	# substitute preparation methods out of name
	for each in bgrams:
		st = each[0] + ' ' + each[1]
		if st in preparations_list:
			remove_prep_from_name = reg.group(9).replace(st, '')
			remove_prep_from_name = remove_prep_from_name.replace('  ', ' ')
			n = {'name': (remove_prep_from_name or '').strip().lower()}
			p = {'preparation': st}
			if '(' in reg.group(9) and ')' in reg.group(9):
				mesPar = re.findall(r'(\(.*?\))', reg.group(9))
				mesWO = mesPar[0][1:-1]
				split2 = mesWO.split()
				for each in split2:
					if each in measurement_list:
						remove_mes_from_name = remove_prep_from_name.replace(mesPar[0], '')
						remove_prep_from_name = remove_prep_from_name.replace('  ', ' ')
						n = {'name': (remove_mes_from_name or '').strip().lower()}
						m = {'measurement': (split2[0] + ' ' + split2[-1] or '').strip()}

		# if engram was enough to make the substitution
		if each[0] in preparations_list:
			remove_prep_from_name2 = reg.group(9).replace(each[0], '')
			remove_prep_from_name2 = remove_prep_from_name2.replace('  ', ' ')
			n = {'name': (remove_prep_from_name2 or '').strip().lower()}
			p = {'preparation': each[0]}
			if '(' in reg.group(9) and ')' in reg.group(9):
				mesPar = re.findall(r'(\(.*?\))', reg.group(9))
				mesWO = mesPar[0][1:-1]
				split2 = mesWO.split()
				for each in split2:
					if each in measurement_list:
						remove_mes_from_name2 = remove_prep_from_name2.replace(mesPar[0], '')
						remove_prep_from_name2 = remove_prep_from_name2.replace('  ', ' ')
						n = {'name': (remove_mes_from_name2 or '').strip().lower()}
						m = {'measurement': (split2[0] + ' ' + split2[-1] or '').strip()}

	# check empty prep for verb phrase
	if p['preparation'] == '':
		t = word_tokenize(reg.group(9))
		x = nltk.pos_tag(t)
		for each in x:
			if 'VB' in each[1]:
				remove_prep_from_name2 = reg.group(9).replace(each[0], '')
				remove_prep_from_name2 = remove_prep_from_name2.replace('  ', ' ')
				n = {'name': (remove_prep_from_name2 or '').strip().lower()}
				p = {'preparation': each[0]}
				if '(' in reg.group(9) and ')' in reg.group(9):
					mesPar = re.findall(r'(\(.*?\))', reg.group(9))
					mesWO = mesPar[0][1:-1]
					split2 = mesWO.split()
					for each in split2:
						if each in measurement_list:
							remove_mes_from_name2 = remove_prep_from_name2.replace(mesPar[0], '')
							remove_prep_from_name2 = remove_prep_from_name2.replace('  ', ' ')
							n = {'name': (remove_mes_from_name2 or '').strip().lower()}
							m = {'measurement': (split2[0] + ' ' + split2[-1] or '').strip()}


	# for each in splitN:
	# 	if each in preparations_list:
	# 		print(each)
	# 		p = {'preparation': each}

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
				m = {'measurement': (splitQ[-1] + ' ' + str(reg.group(6)) or '').strip()}

	if p['preparation'] == '':
		p['preparation'] = 'n/a'

	if "to" in n['name']:
		split_name = word_tokenize(n['name'])
		split_name = ["" if x == "to" else x for x in split_name]
		n['name'] = " ".join(split_name)

	if n['name'] == '':
		n['name'] = reg.group(9).strip().lower()

	if m == {'measurement': ''} or 'None' in m['measurement'] and r'\d' not in m['measurement']:
		splitN = reg.group(9).split()
		for each in splitN:
			if each in measurement_list:
				m = {'measurement': str(each)}

	if q == {'quantity': ''}:
		q = {'quantity': 'n/a'}

	# descriptors
	t = word_tokenize(n['name'])
	d_string = ''
	for each in t:
		if each in descriptors_list:
			d_string += str(each) + ', '
			d = {'descriptor': d_string}
	if d['descriptor'] != '':
		# td = word_tokenize(d_string)
		# for each in td:
		# 	if each in n['name']:
		# 		n['name'] = n['name'].replace(each, '').strip()
		d['descriptor'] = d['descriptor'][0:-2]

	if d['descriptor'] == '':
		d['descriptor'] = 'n/a'

	if m == {'measurement': ''}:
		m = {'measurement': 'n/a'}

	parsed = {**d, **p, **m, **q, **n}

	return parsed

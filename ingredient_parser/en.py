import re

UNITS = {"cup": ["cups", "cup", "c.", "c"],
		 "gill": ["gill", "gills"],
		 "jack": ["jack", "jacks"],
		 "bunch": ["bunch", "bunches"],
		 "fluid ounce": ["fl. oz.", "fl oz", "fl oz.", "fl. oz", "fluid ounce", "fluid ounces"],
		 "gallon": ["gal", "gal.", "gallon", "gallons"],
		 "ounce": ["oz", "oz.", "ounce", "ounces"],
		 "pint": ["pt", "pt.", "pint", "pints"],
		 "fluid pint": ["fl pt", "fl. pt.", "fl. pt", "fl pt.", "fluid pint", "fluid pints"],
		 "pound": ["lb", "lb.", "lbs", "lbs.", "pound", "pounds", "#"],
		 "quart": ["qt", "qt.", "qts", "qts.", "quart", "quarts"],
		 # NOTE: tablespoon can be T as teaspoon can be t
		 "tablespoon": ["tbsp.", "tbsp", "T", "T.", "tablespoon", "tablespoons", "tbs.", "tbs"],
		 # NOTE: teaspoon can be t as tablespoon can be T
		 "teaspoon": ["tsp.", "tsp", "t", "t.", "teaspoon", "teaspoons"],
		 "gram": ["g", "g.", "gr", "gr.", "gram", "grams", "gramme", "grammes"],
		 "kilogram": ["kg", "kg.", "kilogram", "kilograms", "kilogramme", "kilogrammes"],
		 "liter": ["l", "l.", "L", "L.", "liter", "liters", "litre", "litres"],
		 "deciliter": ["dl", "dl.", "dL", "dL.", "deciliter", "deciliters", "decilitre", "decilitres"],
		 "milligram": ["mg", "mg.", "milligram", "milligrams", "milligramme", "milligrammes"],
		 "milliliter": ["ml", "ml.", "milliliter", "milliliters", "millilitre", "millilitres", "cc", "cc.", "CC", "CC.",
						"Cc", "Cc.", "cC", "cC.", "mL", "mL."],
		 "millimeter": ["mm", "mm.", "millimeter", "millimeters", "millimetre", "millimetres"],
		 "centimeter": ["cm", "cm.", "centimeter", "centimeters", "centimetre", "centimetres"],
		 "meter": ["m", "m.", "M", "M.", "meter", "meters", "metre", "metres"],
		 "inch": ["inch", "inches"],
		 "pinch": ["pinch", "pinches"],
		 "dash": ["dash", "dashes"],
		 "touch": ["touch", "touches"],
		 "handful": ["handful", "handfuls"],
		 "stick": ["stick", "sticks"],
		 "clove": ["cloves", "clove"],
		 "can": ["cans", "can"],
		 "large": ["lar", "lar.", "large"],
		 "small": ["sm", "sm.", "small"],
		 "scoop": ["sc", "sc.", "scoop", "scoops"],
		 "fillets": ["filet", "filets", "fillet", "fillets"],
		 "sprig": ["sprig", "sprigs"],
		 "bit": ["bit", "bits"],
		 "few": ["few"],
		 "some": ["some"]
		 }

# tools kb could go here

NUMBERS = ['seventeen', 'eighteen', 'thirteen', 'nineteen', 'fourteen', 'sixteen', 'fifteen', 'seventy', 'twelve',
		   'eleven', 'eighty', 'thirty', 'ninety', 'twenty', 'seven', 'fifty', 'sixty', 'forty', 'three', 'eight',
		   'four', 'zero', 'five', 'nine', 'ten', 'one', 'six', 'two', 'an', 'a']

# possible misspelling
PREPOSITIONS = ["of", "off"]


# a = list(chain.from_iterable(UNITS.values()))
def test(rec):
	for each in rec:
		for one in each:
			yield one


def test2(*rec):
	for each in rec:
		for one in each:
			yield one


a = (test2(UNITS.values()))
b = list(test(a))

# not necessary?
# b.sort(key=lambda x: len(x), reverse=True)

# a = map(escape_re_string, a)
# not working?
for each in b:
	each.replace('.', '\.')
	each.replace('(', '')
	each.replace(')', '')
	re.sub(r'\s+', ' ', each)

PARSER_RE = re.compile(
	r'(?P<quantity>(?:[\d\.,][\d\.,\s/]*)?\s*(?:(?:%s)\s*)*)?(\s*(?P<unit>%s)\s+)?(\s*(?:%s)\s+)?(\s*(?P<name>.+))?' % (
		'|'.join(NUMBERS), '|'.join(b), '|'.join(PREPOSITIONS)))


# PARSER_RE = re.compile(
# 	r'(?P<quantity>(?:[(0-9)\.,][\d\.,\s/]*)?[\r\n\t\f\v ]*(?:(?:%s)[\r\n\t\f\v ]*)*)?([\r\n\t\f\v ]*(?P<unit>%s)[\r\n\t\f\v ]+)?([\r\n\t\f\v ]*(?:%s)[\r\n\t\f\v ]+)?([\r\n\t\f\v ]*(?P<name>.+))?' % (
# 	'|'.join(NUMBERS), '|'.join(b), '|'.join(PREPOSITIONS)))


def parse(st):
	"""

	:param st:
	:return:
	"""
	# st = normalize(st)
	st = re.sub(r'\s', ' ', re.compile(r'^([\d\s*[\d\.,/]*)\s*(.+)').sub('\g<1> \g<2>', st)).strip()
	res = PARSER_RE.match(st)

	return {
		'Name': (res.group('name') or '').strip().lower(),
		'Quantity': (res.group('quantity') or '').strip().lower(),
		# 'Measurement': (res.group('quantity') or '').strip() + ' ' + (res.group('unit') or '').strip(),
		'Units': (res.group('unit') or '').strip(),
		# 'Tools': (res.group('tools') or '').strip().lower(),
	}

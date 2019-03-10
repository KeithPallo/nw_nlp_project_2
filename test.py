import re

# string = '2 9/2 '
# x = string.split(' ')
# print(x[0])
# print(x[-2])
# print(x[-1])
# print(x[0])
# x = x[0:-1]
# print(x)
# if '/' in x[-1]:
# 	print(True)
# else:
# 	print(False)

st = '(9 inch) pizzas'
x = ['inch', 'foot']

if '(' in st:
	mes1 = re.findall(r'(\(.*?\))', st)
	mes2 = mes1[0][1:-1]
	print(mes1[0])
	print(mes2)
	split2 = mes2.split()
	print(split2)
	for each in split2:
		if each in x:
			print(split2[0])
			print(split2[-1])
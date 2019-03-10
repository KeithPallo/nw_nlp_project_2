import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
01234567890

Ha ha Haha Hahaha haHaha

Meta characters:
. ^ & * + ? { } [ ] \ | ( )

coreyms.com
cat
mat
pat
bat

321-.555-.4321
321-555-4321
123.555.1234
123*555*3214
800-555-4321
900-555-4321

Mr. Schafer
Mr Smith
Ms Davis
Mrs Robinson
Mr. T

CoreyMShafer@gmail.com
corey.shafer@university.edu
corey-321-schaafter@my----werweworjoidjfoweijf283913j92j3i-work.net.weoiowifaweofi

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'\d')

matches = pattern.finditer(text_to_search)
print('')

for match in matches:
	print(match)
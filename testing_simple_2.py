import bs4 as bs
import requests
from pprint import pprint


#url = "https://www.allrecipes.com/recipes/14452/everyday-cooking/special-collections/hall-of-fame/?page=2"
# url = "https://www.allrecipes.com/recipes/1642/everyday-cooking/?internalSource=hub%20nav&referringId=14452&referringContentType=Recipe%20Hub&referringPosition=1&linkName=hub%20nav%20exposed&clickId=hub%20nav%203&page=2"
url = "https://www.allrecipes.com/recipes/1899/world-cuisine/asian/chinese/appetizers/?internalSource=hub%20nav&referringId=695&referringContentType=Recipe%20Hub&linkName=hub%20nav%20daughter&clickId=hub%20nav%202"
# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
soup = bs.BeautifulSoup(data, 'lxml')

# Extracting all the <a> tags into a list.
tags = soup.find_all('a')

links = []
print(len(tags))
# Extracting URLs from the attribute href in the <a> tags.
for tag in tags:
    x = tag.get('href')
    print(x)
    if not x: x = "none"
    if "/recipe/" in x and x not in links:
        links.append(x)

pprint(links)
pprint(len(links))

import json


veggie = []
health = []
unheathly = []
# Custom cuisine mappings

def write_urls(urls,output_file):

    for url in urls:
        response = requests.get(url)

        # Extracting the source code of the page.
        data = response.text

        # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
        soup = bs.BeautifulSoup(data, 'lxml')

        # Extracting all the <a> tags into a list.
        tags = soup.find_all('a')

        links = []

        # Extracting URLs from the attribute href in the <a> tags.
        for tag in tags:
            x = tag.get('href')
            if not x: x = "none"

            if "/recipe/" in x and x not in links and x != "none":
                links.append(x)

        # write links to output file
        with open(output_file, 'a+') as outfile:
            json.dump(links, outfile)

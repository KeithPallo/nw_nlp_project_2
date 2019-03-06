import json
import bs4 as bs
import requests

veggie = ["https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/"]
health = ["https://www.allrecipes.com/recipes/84/healthy-recipes/","https://www.allrecipes.com/recipes/739/healthy-recipes/diabetic/",
          "https://www.allrecipes.com/recipes/742/healthy-recipes/low-carb/", "https://www.allrecipes.com/recipes/22485/healthy-recipes/heart-healthy-recipes/",
          "https://www.allrecipes.com/recipes/1232/healthy-recipes/low-calorie/","https://www.allrecipes.com/recipes/1231/healthy-recipes/low-fat/",
          "https://www.allrecipes.com/recipes/22607/healthy-recipes/weight-loss/"]
unheathly = []
# To add - Custom cuisine mappings

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
        try:
            with open(output_file, 'r') as outfile:
                prev = json.load(outfile)
            prev.extend(links)
            links = prev

        except:
            pass

        with open(output_file, 'w') as outfile:
            json.dump(links, outfile)


# Standard run call

if __name__ == "__main__":
    # write_urls(veggie, "json_created_files/veggie_links.json")
    write_urls(health, "json_created_files/health_links.json")

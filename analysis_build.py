from parse_url import *

url1 = 'https://www.allrecipes.com/recipe/228293' # Test url - currently not in use


# Step 0 - Call mapping_json_make from command line to create search URLS
# Command Line Call: python mapping_urls_make.py

# Point at URLS to build from - List of Tuples. Tuple = (filename,target_url)
# Note - add in tuples to add in analysis, but remove or delete files to avoid multiplicity
urls = [("json_created_files/veggie_links.json","json_created_files/veggie")]


# Call main parse on each of the sections from above

for run in urls:
    file = run[0]
    name = run[1]

    # Create Individual URL List
    with open(file, 'r') as infile:
        ind_url_list = json.load(infile)

    # Potentially remove duplicates

    for ind_url in ind_url_list:
        main_parse(ind_url,check="false",url_name="json_created_files/veggie")

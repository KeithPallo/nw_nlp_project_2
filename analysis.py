from parse_file import *

url1 = 'https://www.allrecipes.com/recipe/228293' # Test url

# Call test_json_read to make lists of URLS from different categories

# Get lists of urls
# Ideally, read from JSON(s) created from previous section

# Call main parse to parse each of the URL's previous collectioned
main_parse(url1,check="false",url_name="veggie")

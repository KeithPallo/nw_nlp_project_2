# nw_nlp_project_2
Recipe Builder

Team Members: Ikhlas Attarwala, Mario Lizano, Yi Qiao, Keith Pallo


# System Requirements

The following packages are required to run the code

### NLTK
sudo pip install -U nltk  
https://www.nltk.org/install.html

### Pandas
pip install pandas   
https://pandas.pydata.org/

### Numpy
sudo pip install -U numpy  
https://www.numpy.org/



# Instructions

First clone the repo.

Then go to the following link. Download the file "allrecipes-recipes.json" and place it in your working directory.

https://drive.google.com/file/d/1EFl6ch20jAj0T5XTt0QPplCKFHPFKp-k/view?usp=sharing

From the command line run the following command:

`python3 main_run.py`

This will prompt you to put in a valid url from AllRecipes.com, and will allow you to run multiple transforms on a single recipe.

While running the program, a file called test.txt will be created that will record a human readable version of the changed ingredients in a recipe, and the new directions that are created. This file appends the new result to itself when running the program - so multiple recipe outputs and transforms can be examined following the successful completion of the main code.

# Statistical Methods

During this project, our team worked hard to make a generalizable method to map recipes to any cuisine - given a large corpus of recipes from said cuisine (which is our "training data"). For example, given a large corpus of Italian recipes we wanted to be able to automatically be able to transform any recipe into the Italian target. We have done this, and our methodology has been shown in the Jupyter Notebook cuisine_transformation.ipynb.

Given the recipes we could find, we made 6 distinct transformations (which are implemented in main_run) as they presented what we believed a large enough corpus - but this could be easily extended with more recipes.

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


# Methodologies
We had three different approaches to the three different recipe transformation tasks that we handled. However, the similarity in all of our methodologies was the use of ingredients KBs that were used to identify which ingredients to replace. The biggest limitation in our code was probably the completeness of these ingredients KBs, because it was difficult to account for every possible ingredient that could appear. However, if desired, the KBs can easily be extended to obtain more accurate transformations.

## Unhealthy to Healthy and vice versa
Our Unhealthy and Healthy methods are fairly simple in that they categorize each ingredient seen into a larger type of ingredient (for example olive oil is in the cooking fats group), and then we apply a simple list of rules to that type of category - for example, swap out for a healthy protein, or replace sugar with low calorie artificial sweeteners. To keep it simple - this is a one to one ingredient swap. For the directions parsing, we then replace the associated ingredients by looking for the longest version of the original ingredients using an n-gram analysis.


## Non-vegetarian to Vegetarian and vice versa
write me

## Cuisines - Statistical Methods

During this project, our team worked hard to make a generalizable method to map recipes to any cuisine - given a large corpus of recipes from said cuisine (which is our "training data"). For example, given a large corpus of Italian recipes we wanted to be able to automatically be able to transform any recipe into the Italian target. We have done this, and our methodology has been shown in the Jupyter Notebook cuisine_transformation.ipynb.

Given the recipes we could find, we made 6 distinct transformations (which are implemented in main_run) as they presented what we believed a large enough corpus - but this could be easily extended with more recipes.

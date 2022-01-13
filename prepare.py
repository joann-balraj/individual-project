## Individual Project Prepare File ##
#### 10000 Most Common Passwords ####

# This module is going to be where I will put all my functions for acquiring and preparing the data
# for my individual project, in order to keep the final report as simple as possible. 


### Imports ###
import pandas as pd 

############### Acquire Data ###############
def get_data():
    """
    This first function will acquire the data from 
    """
    df = pd.read_csv("common_passwords.csv")
    return df

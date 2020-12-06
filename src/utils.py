import pickle as pkl
import csv
import tensorflow as tf
import numpy as np
import random   
import pandas as pd

# Function to reset seeds for the sake of consistency
def reset_seeds():
    SEED = 100
    np.random.seed(SEED)
    tf.random.set_seed(SEED)
    random.seed(SEED)

def dict_to_csv(input_dict, filename):
    pd.DataFrame.from_dict(data=input_dict, orient='index').to_csv(filename, header=False)
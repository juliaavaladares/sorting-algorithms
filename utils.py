import pandas as pd

def getDados():
    database = pd.read_csv("dataset.csv")
    print(database.shape)
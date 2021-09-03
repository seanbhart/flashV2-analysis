import pandas as pd

from utils import stakes


filename = './data/flashstake_data-2021-08-23.csv'


def getFlashData() -> pd.DataFrame:
    return pd.read_csv(filename)

def importFlashData():
    stakes.stakes_to_db(filename)

# print(getFlashData())
importFlashData()

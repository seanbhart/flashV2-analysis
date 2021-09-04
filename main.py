import pandas as pd

from utils import dex
from utils import stakes


uniswap_filename = './data/flashV2-2021-liq.csv'
stake_filename = './data/flashstake_data-2021-08-23.csv'


def getFlashData() -> pd.DataFrame:
    return pd.read_csv(stake_filename)

def importUniswapData():
    dex.uniswap_to_db(uniswap_filename)

def importFlashData():
    stakes.stakes_to_db(stake_filename)

# print(getFlashData())
importUniswapData()
# importFlashData()

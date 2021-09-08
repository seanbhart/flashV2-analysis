import pandas as pd

from utils import dex
from utils import stakes


ethpx_filename = './data/ethpx.csv'
uniswap_filename = './data/flashV2-2021-liq.csv'
uniswap_tx_filename = './data/flash6.csv'
stake_filename = './data/flashstake_data-2021-08-23.csv'


def getFlashData() -> pd.DataFrame:
    return pd.read_csv(stake_filename)

def importUniswapData():
    dex.uniswap_to_db(uniswap_filename)

def importUniswapTxData():
    dex.uniswap_tx_to_db(uniswap_tx_filename)

def importEthPxData():
    dex.ethpx_to_db(ethpx_filename)

def importFlashData():
    stakes.stakes_to_db(stake_filename)

# print(getFlashData())
# importUniswapData()
# importUniswapTxData()
importEthPxData()
# importFlashData()

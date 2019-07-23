import numpy as np
import pandas as pd

KIBOT_ETFS = "/home/yury/repo/alphatrai/utils/kibot-alletfs-1day-adjusted"
KIBOT_STOCKS = "/home/yury/repo/alphatrai/utils/kibot-allstocks-1day-adjusted"

def load_daily(ticker):

    for data_dir in [KIBOT_ETFS, KIBOT_STOCKS]:
        try:
            ticker_path = f"{data_dir}/{ticker}.csv.gz"
            df = pd.read_csv(ticker_path, usecols=[0,1,2,3,4,5])
        except:
            continue
        break

    df.columns = ('date', 'open', 'high', 'low', 'close', 'volume')

    # set the dataframe to have a datetime index
    df.index = pd.DatetimeIndex(df['date'])

    # name the index and columns
    df.index.name = 'date'
    df.columns.name = ticker

    del df['date']

    # make sure time goes forward regardless of whether we ffill
    df = df.sort_index()

    return df

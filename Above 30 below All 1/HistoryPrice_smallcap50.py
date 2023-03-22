from datetime import date
import sys
import pandas as pd
from nsepy import get_history


def process_trade(trade_list):
    with open('smallcap50.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print('This message will be written to a file.')
        for trade in trade_list:
            data = get_history(symbol=trade, start=date(2020, 1, 1), end=date.today())
            df =""
            df = pd.DataFrame(data, columns=['Symbol', 'Series', 'Prev Close', 'Close', 'Volume'])
            df7 = pd.DataFrame(data, columns=['Close'])
            short_rolling3 = df7.rolling(window=3).mean()
            df['avgPrice3'] = short_rolling3
            short_rolling10 = df7.rolling(window=10).mean()
            df['avgPrice10'] = short_rolling10
            short_rolling30 = df7.rolling(window=30).mean()
            df['avgPrice30'] = short_rolling30
            short_rolling50 = df7.rolling(window=50).mean()
            df['avgPrice50'] = short_rolling50
            short_rolling200 = df7.rolling(window=200).mean()
            df['avgPrice200'] = short_rolling200

            ds = ""
            for i in df.index:
                if df.loc[i, 'avgPrice10'] >= df.loc[i, 'Close'] >= df.loc[i, 'avgPrice30'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice200'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice50']:

                    ls = str(i) + ": " + str(df.loc[i, 'Symbol']) \
                         + " Close: " + str(df.loc[i, 'Close']) \
                         + " avgPrice10 " + str(round(df.loc[i, 'avgPrice10'])) \
                         + " avgPrice30 " + str(round(df.loc[i, 'avgPrice30'])) \
                         + " avgPrice50 " + str(round(df.loc[i, 'avgPrice50'])) \
                         + " avgPrice200 " + str(round(df.loc[i, 'avgPrice200'])) \
                         + " Vol " + str(round(df.loc[i, 'Volume']))
                    ds = ds + ls + '\n'
                    ls = ''
            print(ds)
            # sys.stdout = original_std_out

        # Large Cap
trade_list = ['ECLERX','MRPL','SWANENERGY','OLECTRA','JBMA','POLYMED','PRSMJOHNSN','ROUTE','ENGINERSIN','LEMONTREE','GREENPANEL','MEDPLUS','ZYDUSWELL','NBCC','CERA','ANGELONE','MAHLOG','SWSOLAR','RATNAMANI','KALPATPOWR','PNCINFRA','GLENMARK','JSL','TTKPRESTIG','APTUS','CDSL','THYROCARE','IFBIND','MAPMYINDIA','NLCINDIA','KIMS','BALRAMCHIN','VARROC','ASTERDM','WELSPUNIND','CHALET','CEATLTD','DCMSHRIRAM','TRITURBINE','SUPRAJIT','LUXIND','CAMPUS','VGUARD','CREDITACC','RVNL','NCC','CHOLAHLDNG','CENTURYTEX','WELCORP','SUDARSCHEM']

process_trade(trade_list)

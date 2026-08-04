import requests
import pandas as pd
import time
import os


SYMBOL = "BTCUSDT"
INTERVAL = "1h"

START_TIME = int(
    pd.Timestamp("2018-01-01").timestamp() * 1000
)


END_TIME = int(
    pd.Timestamp.now().timestamp() * 1000
)



def download_binance_history():


    print("==============================")
    print("BINANCE HISTORY DOWNLOADER")
    print("==============================")


    url = (
        "https://api.binance.com/api/v3/klines"
    )


    all_data = []

    current = START_TIME



    while current < END_TIME:


        params = {

            "symbol": SYMBOL,

            "interval": INTERVAL,

            "startTime": current,

            "limit": 1000

        }


        response = requests.get(
            url,
            params=params
        )


        candles = response.json()



        if not candles:

            break



        for c in candles:

            all_data.append(

                [

                    c[0],

                    c[1],

                    c[2],

                    c[3],

                    c[4],

                    c[5]

                ]

            )



        current = candles[-1][0] + 1



        print(
            "Loaded candles:",
            len(all_data)
        )


        time.sleep(0.2)



    df = pd.DataFrame(

        all_data,

        columns=[

            "time",

            "open",

            "high",

            "low",

            "close",

            "volume"

        ]

    )



    df.to_csv(

        "data/history.csv",

        index=False

    )



    print("==============================")

    print(
        "HISTORY SAVED"
    )

    print(
        "TOTAL:",
        len(df)
    )

    print("==============================")



if __name__ == "__main__":

    download_binance_history()
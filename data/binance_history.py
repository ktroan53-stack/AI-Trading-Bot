import requests
import pandas as pd
import time
import os
from datetime import datetime


SYMBOL = "BTCUSDT"

INTERVAL = "1h"

START_DATE = "2018-01-01"

LIMIT = 1000


SAVE_PATH = "data/BTCUSDT_1h_history.csv"



def date_to_ms(date):

    dt = datetime.strptime(
        date,
        "%Y-%m-%d"
    )

    return int(
        dt.timestamp() * 1000
    )



def download_candles():


    start_time = date_to_ms(
        START_DATE
    )


    all_data = []


    print("==============================")
    print("BINANCE HISTORY DOWNLOADER")
    print("==============================")

    print(
        f"Symbol: {SYMBOL}"
    )

    print(
        f"Interval: {INTERVAL}"
    )

    print(
        f"Start: {START_DATE}"
    )


    while True:


        url = (
            "https://api.binance.com/api/v3/klines"
        )


        params = {

            "symbol": SYMBOL,

            "interval": INTERVAL,

            "startTime": start_time,

            "limit": LIMIT

        }


        response = requests.get(
            url,
            params=params
        )


        data = response.json()



        if not data:

            break



        all_data.extend(
            data
        )


        last_time = data[-1][0]


        start_time = (
            last_time + 1
        )


        current_date = datetime.fromtimestamp(
            last_time / 1000
        )


        print(
            "Downloaded:",
            len(all_data),
            "candles |",
            current_date
        )



        if len(data) < LIMIT:

            break



        time.sleep(
            0.3
        )



    return all_data





def save_data(data):


    df = pd.DataFrame(
        data,
        columns=[

            "time",
            "open",
            "high",
            "low",
            "close",
            "volume",

            "close_time",

            "quote_volume",

            "trades",

            "taker_buy_base",

            "taker_buy_quote",

            "ignore"

        ]

    )


    df = df[

        [
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume"

        ]

    ]



    numeric = [

        "open",
        "high",
        "low",
        "close",
        "volume"

    ]



    df[numeric] = df[numeric].astype(
        float
    )



    df.to_csv(
        SAVE_PATH,
        index=False
    )



    print("==============================")
    print("HISTORY SAVED")
    print("==============================")

    print(
        SAVE_PATH
    )


    print(
        "Rows:",
        len(df)
    )





def main():


    candles = download_candles()


    save_data(
        candles
    )




if __name__ == "__main__":

    main()
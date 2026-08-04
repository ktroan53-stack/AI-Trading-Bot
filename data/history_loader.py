import pandas as pd
import requests
import time


class HistoryLoader:
    """
    Загрузчик исторических данных

    Получает свечи Binance API

    Поддерживает:
    - BTCUSDT
    - ETHUSDT
    - таймфреймы
    """



    def __init__(
        self,
        symbol="BTCUSDT",
        interval="1h"
    ):

        self.symbol = symbol

        self.interval = interval

        self.url = (
            "https://api.binance.com/api/v3/klines"
        )



    def load(
        self,
        limit=1000
    ):


        params = {

            "symbol":
                self.symbol,

            "interval":
                self.interval,

            "limit":
                limit

        }


        response = requests.get(

            self.url,

            params=params

        )


        data = response.json()



        candles = []


        for row in data:


            candles.append({

                "time":
                    row[0],

                "open":
                    float(row[1]),

                "high":
                    float(row[2]),

                "low":
                    float(row[3]),

                "close":
                    float(row[4]),

                "volume":
                    float(row[5])

            })


        df = pd.DataFrame(
            candles
        )


        return df



    def save(
        self,
        df,
        filename="data/history.csv"
    ):


        df.to_csv(

            filename,

            index=False

        )


        print(
            "History saved:"
        )

        print(
            filename
        )



if __name__ == "__main__":


    loader = HistoryLoader(

        symbol="BTCUSDT",

        interval="1h"

    )


    df = loader.load(
        limit=1000
    )


    loader.save(
        df
    )


    print(
        df.head()
    )
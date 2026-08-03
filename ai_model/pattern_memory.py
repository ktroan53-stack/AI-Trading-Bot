import json
import os
from datetime import datetime


class PatternMemory:
    """
    Память рынка AI Trading Bot

    Хранит:
    - рыночные ситуации
    - паттерны
    - результат сделок
    - статистику поведения

    Используется для:
    - поиска закономерностей
    - обучения AI
    """



    def __init__(
        self,
        file_path="ai_model/patterns.json"
    ):

        self.file_path = file_path

        self.patterns = []

        self.load()



    def load(self):

        if os.path.exists(
            self.file_path
        ):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.patterns = json.load(file)



    def save(self):

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.patterns,
                file,
                indent=4,
                ensure_ascii=False
            )



    def add_pattern(
        self,
        market_data,
        signal,
        result
    ):


        pattern = {

            "time":
                str(datetime.now()),


            "market":

                market_data,


            "signal":

                signal,


            "result":

                result

        }


        self.patterns.append(
            pattern
        )


        self.save()



    def analyze_patterns(self):

        statistics = {

            "LONG": {

                "wins":0,

                "losses":0

            },


            "SHORT": {

                "wins":0,

                "losses":0

            }

        }



        for pattern in self.patterns:


            signal = pattern["signal"]

            result = pattern["result"]



            if signal in statistics:


                if result > 0:

                    statistics[signal]["wins"] += 1


                else:

                    statistics[signal]["losses"] += 1



        return statistics



    def find_best_patterns(
        self
    ):


        stats = self.analyze_patterns()


        best = []


        for signal,data in stats.items():

            total = (
                data["wins"]
                +
                data["losses"]
            )


            if total > 0:

                winrate = (
                    data["wins"]
                    /
                    total
                    *
                    100
                )


                best.append({

                    "signal":
                        signal,

                    "winrate":
                        round(
                            winrate,
                            2
                        )

                })


        return best
import datetime


def get_market_status():
    """
    Проверка работы модуля данных
    """

    time_now = datetime.datetime.now()

    print("Модуль рыночных данных запущен")
    print("Время проверки:", time_now)


if __name__ == "__main__":
    get_market_status()
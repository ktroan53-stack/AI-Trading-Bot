import pandas as pd


def calculate_adx(data, period=14):
    """
    Average Directional Index (ADX)

    Показывает силу тренда:
    
    < 20  слабый тренд
    20-40 нормальный тренд
    > 40 сильный тренд
    """


    high = data["high"]

    low = data["low"]

    close = data["close"]



    # True Range

    tr = pd.DataFrame()

    tr["high_low"] = high - low

    tr["high_close"] = abs(
        high - close.shift()
    )

    tr["low_close"] = abs(
        low - close.shift()
    )


    true_range = tr.max(
        axis=1
    )



    # Directional Movement

    plus_dm = high.diff()

    minus_dm = low.diff() * -1



    plus_dm[
        plus_dm < 0
    ] = 0


    minus_dm[
        minus_dm < 0
    ] = 0



    # Smoothed values

    atr = true_range.rolling(
        period
    ).mean()


    plus_di = (
        100 *
        plus_dm.rolling(period).mean()
        /
        atr
    )


    minus_di = (
        100 *
        minus_dm.rolling(period).mean()
        /
        atr
    )



    dx = (
        abs(
            plus_di - minus_di
        )
        /
        (
            plus_di + minus_di
        )
    ) * 100



    adx = dx.rolling(
        period
    ).mean()



    return adx
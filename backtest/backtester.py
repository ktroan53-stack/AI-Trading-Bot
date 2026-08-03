import pandas as pd


class Backtester:
    """
    Базовый движок тестирования стратегий
    AI Trading Bot
    """

    def __init__(self, initial_balance=10000):

        self.initial_balance = initial_balance
        self.balance = initial_balance

        self.trades = []

        self.position = None


    def open_trade(
        self,
        date,
        side,
        price,
        quantity
    ):

        if self.position is not None:
            return False

        self.position = {
            "date": date,
            "side": side,
            "entry_price": price,
            "quantity": quantity
        }

        return True


    def close_trade(
        self,
        date,
        price
    ):

        if self.position is None:
            return False


        entry = self.position["entry_price"]
        quantity = self.position["quantity"]
        side = self.position["side"]


        if side == "LONG":
            pnl = (price - entry) * quantity

        else:
            pnl = (entry - price) * quantity


        self.balance += pnl


        trade = {
            "open_date": self.position["date"],
            "close_date": date,
            "side": side,
            "entry": entry,
            "exit": price,
            "quantity": quantity,
            "pnl": round(pnl, 2)
        }


        self.trades.append(trade)

        self.position = None

        return True



    def calculate_results(self):

        if len(self.trades) == 0:

            return {
                "Trades": 0,
                "Balance": self.balance
            }


        df = pd.DataFrame(self.trades)


        wins = df[df["pnl"] > 0]
        losses = df[df["pnl"] < 0]


        win_rate = (
            len(wins) /
            len(df) *
            100
        )


        profit_factor = (
            wins["pnl"].sum()
            /
            abs(losses["pnl"].sum())
            if len(losses) > 0
            else 0
        )


        return {

            "Trades": len(df),

            "Final Balance":
                round(self.balance,2),

            "Profit":
                round(
                    self.balance -
                    self.initial_balance,
                    2
                ),

            "Win Rate":
                round(win_rate,2),

            "Profit Factor":
                round(profit_factor,2)

        }


    def get_trades(self):

        return self.trades
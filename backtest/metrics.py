import numpy as np


class PerformanceMetrics:
    """
    Математический анализ эффективности стратегии
    AI Trading Bot
    """

    def __init__(self, trades):

        self.trades = trades


    def total_profit(self):

        return round(
            sum(
                trade["pnl"]
                for trade in self.trades
            ),
            2
        )


    def win_rate(self):

        if len(self.trades) == 0:
            return 0


        wins = [
            t for t in self.trades
            if t["pnl"] > 0
        ]


        return round(
            len(wins) /
            len(self.trades) *
            100,
            2
        )


    def expectancy(self):

        """
        Математическое ожидание одной сделки
        """

        if len(self.trades) == 0:
            return 0


        profits = [
            t["pnl"]
            for t in self.trades
            if t["pnl"] > 0
        ]


        losses = [
            t["pnl"]
            for t in self.trades
            if t["pnl"] < 0
        ]


        win_probability = (
            len(profits) /
            len(self.trades)
        )


        loss_probability = (
            len(losses) /
            len(self.trades)
        )


        average_win = (
            np.mean(profits)
            if profits
            else 0
        )


        average_loss = (
            abs(np.mean(losses))
            if losses
            else 0
        )


        result = (
            win_probability *
            average_win
            -
            loss_probability *
            average_loss
        )


        return round(result, 4)



    def profit_factor(self):

        profit = sum(
            t["pnl"]
            for t in self.trades
            if t["pnl"] > 0
        )


        loss = abs(
            sum(
                t["pnl"]
                for t in self.trades
                if t["pnl"] < 0
            )
        )


        if loss == 0:
            return 0


        return round(
            profit / loss,
            2
        )



    def max_drawdown(self):

        balance = 0
        peak = 0
        max_dd = 0


        for trade in self.trades:

            balance += trade["pnl"]

            if balance > peak:
                peak = balance


            drawdown = peak - balance


            if drawdown > max_dd:
                max_dd = drawdown


        return round(
            max_dd,
            2
        )



    def sharpe_ratio(self):

        returns = [
            trade["pnl"]
            for trade in self.trades
        ]


        if len(returns) < 2:
            return 0


        mean = np.mean(returns)

        std = np.std(returns)


        if std == 0:
            return 0


        return round(
            mean / std,
            3
        )



    def summary(self):

        return {

            "Total Profit":
                self.total_profit(),

            "Win Rate %":
                self.win_rate(),

            "Expectancy":
                self.expectancy(),

            "Profit Factor":
                self.profit_factor(),

            "Max Drawdown":
                self.max_drawdown(),

            "Sharpe Ratio":
                self.sharpe_ratio()

        }
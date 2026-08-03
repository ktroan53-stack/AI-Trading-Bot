class PerformanceTracker:
    """
    Статистика торговли AI Trading Bot
    """

    def __init__(self):

        self.total_trades = 0
        self.wins = 0
        self.losses = 0

        self.total_profit = 0.0
        self.total_loss = 0.0

        self.win_streak = 0
        self.loss_streak = 0

        self.max_win_streak = 0
        self.max_loss_streak = 0

    def add_trade(self, pnl):

        self.total_trades += 1

        if pnl > 0:

            self.wins += 1
            self.total_profit += pnl

            self.win_streak += 1
            self.loss_streak = 0

            self.max_win_streak = max(
                self.max_win_streak,
                self.win_streak
            )

        else:

            self.losses += 1
            self.total_loss += abs(pnl)

            self.loss_streak += 1
            self.win_streak = 0

            self.max_loss_streak = max(
                self.max_loss_streak,
                self.loss_streak
            )

    def win_rate(self):

        if self.total_trades == 0:
            return 0

        return round(
            self.wins / self.total_trades * 100,
            2
        )

    def profit_factor(self):

        if self.total_loss == 0:
            return 0

        return round(
            self.total_profit / self.total_loss,
            2
        )

    def average_profit(self):

        if self.wins == 0:
            return 0

        return round(
            self.total_profit / self.wins,
            2
        )

    def average_loss(self):

        if self.losses == 0:
            return 0

        return round(
            self.total_loss / self.losses,
            2
        )

    def summary(self):

        return {
            "Trades": self.total_trades,
            "Wins": self.wins,
            "Losses": self.losses,
            "Win Rate": self.win_rate(),
            "Profit Factor": self.profit_factor(),
            "Average Profit": self.average_profit(),
            "Average Loss": self.average_loss(),
            "Max Win Streak": self.max_win_streak,
            "Max Loss Streak": self.max_loss_streak
        }
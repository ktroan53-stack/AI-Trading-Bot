from risk.modes import RISK_MODES


class RiskManager:
    """
    Управление рисками AI Trading Bot
    """

    def __init__(self, balance=10000, mode="BALANCED"):

        self.balance = balance
        self.mode = mode

        settings = RISK_MODES[mode]

        self.risk_per_trade = settings["risk_per_trade"]
        self.max_daily_loss = settings["max_daily_loss"]
        self.max_drawdown = settings["max_drawdown"]
        self.max_positions = settings["max_positions"]

    def calculate_position_size(self, entry_price, stop_loss):

        risk_amount = self.balance * self.risk_per_trade

        stop_distance = abs(entry_price - stop_loss)

        if stop_distance == 0:
            return 0

        position_size = risk_amount / stop_distance

        return round(position_size, 4)

    def can_open_trade(self):
        return True

    def get_info(self):

        return {
            "mode": self.mode,
            "balance": self.balance,
            "risk_per_trade": self.risk_per_trade,
            "max_daily_loss": self.max_daily_loss,
            "max_drawdown": self.max_drawdown,
            "max_positions": self.max_positions
        }
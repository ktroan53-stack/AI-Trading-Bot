class PositionManager:
    """
    Управление торговыми позициями
    """

    def __init__(self, balance, leverage=1, max_positions=3):

        self.balance = balance
        self.leverage = leverage
        self.max_positions = max_positions
        self.open_positions = []

    def can_open_position(self):

        return len(self.open_positions) < self.max_positions

    def calculate_position_value(self, risk_amount, stop_percent):

        if stop_percent <= 0:
            return 0

        return round(risk_amount / stop_percent, 2)

    def calculate_quantity(self, position_value, entry_price):

        if entry_price <= 0:
            return 0

        quantity = (position_value * self.leverage) / entry_price

        return round(quantity, 6)

    def open_position(
        self,
        symbol,
        side,
        entry_price,
        stop_loss,
        take_profit,
        quantity
    ):

        if not self.can_open_position():
            return False

        position = {
            "symbol": symbol,
            "side": side,
            "entry": entry_price,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "quantity": quantity
        }

        self.open_positions.append(position)

        return True

    def close_position(self, symbol):

        for position in self.open_positions:

            if position["symbol"] == symbol:

                self.open_positions.remove(position)

                return True

        return False

    def get_open_positions(self):

        return self.open_positions

    def total_positions(self):

        return len(self.open_positions)
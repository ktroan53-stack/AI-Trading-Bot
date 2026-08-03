"""
Режимы управления риском
"""

RISK_MODES = {

    "CONSERVATIVE": {
        "risk_per_trade": 0.01,
        "max_daily_loss": 0.03,
        "max_drawdown": 0.10,
        "max_positions": 2
    },

    "BALANCED": {
        "risk_per_trade": 0.02,
        "max_daily_loss": 0.05,
        "max_drawdown": 0.15,
        "max_positions": 4
    },

    "AGGRESSIVE": {
        "risk_per_trade": 0.03,
        "max_daily_loss": 0.08,
        "max_drawdown": 0.25,
        "max_positions": 6
    }

}
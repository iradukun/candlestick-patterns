class CandleStick:
    def __init__(self, data: dict):
        self.open = data["open"]
        self.close = data["close"]
        self.high = data["high"]
        self.low = data["low"]
        self.volume = data["volume"]
        self.date = data["date"]

    def __repr__(self):
        return (f"CandleStick(open={self.open}, close={self.close},"
                f" high={self.high}, low={self.low}, volume={self.volume}")
  
    def is_bullish(self):
        return self.open < self.close
  
    def is_bearish(self):
        return self.open > self.close
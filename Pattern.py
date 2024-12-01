import CandleStick
class SingleCandlePattern(CandleStick):
    """Pattern formed by the single candle."""

    def is_hammer(self):
        """The Hammer is a bullish reversal pattern."""
        return self.is_bullish() and bool(self.lowerWick >= 2 * self.bodyLength > self.upperWick >= 0)
    
    def is_hanging_man(self):
        """The Hanging Man is a bearish reversal pattern."""
        return self.is_bearish() and bool(self.lowerWick >= 2 * self.bodyLength > self.upperWick >= 0)
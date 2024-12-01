class SingleCandlePattern(CandleStick):
    """Pattern formed by the single candle."""

    def is_doji(self):
        """Doji - When Open price = Close price."""
        return self.open == self.close
    
    def is_four_price_doji(self):
        """Doji - When Open price = Close = low = High price."""
        return self.is_doji() and (self.high == self.low == self.open)

    def is_long_legged_doji(self):
        """upperWick is smaller than lowerWick."""
        return self.is_doji() and self.upperWick < self.lowerWick

    def is_gravestone_doji(self):
        """
        Long Upper wick/shadow and no lower wick.
        Gravestone doji 
        """
        return self.is_doji() and (self.lowerWick == 0 or self.upperWick >= 3*self.lowerWick)

    def is_dragonfly_doji(self):
        """
        Long Lower wick/shadow and no upper wick; looks like "T"
        Bullish dragonfly doji.
        """
        return self.is_doji() and (self.upperWick == 0 or self.lowerWick >= 3*self.upperWick)
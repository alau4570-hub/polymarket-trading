class ETHBot:
    def __init__(self, price_feed, strategy, execution_engine):
        self.price_feed = price_feed
        self.strategy = strategy
        self.execution_engine = execution_engine

    def run(self):
        # Retrieve the current price
        current_price = self.price_feed.get_price()
        # Determine the action based on strategy
        action = self.strategy.decide_action(current_price)
        # Execute the trade
        self.execution_engine.execute(action)

# Example usage:
# price_feed = PriceFeed(api_key)
# strategy = TradingStrategy()
# execution_engine = ExecutionEngine(api_key)
# eth_bot = ETHBot(price_feed, strategy, execution_engine)
# eth_bot.run()
https://import JTrade
import time

if __name__ == "__main__":
    print("JTrade module loaded successfully!")

    JTrade.main()

    while True:
        time.sleep(1)
SC_NODE_URL=https://bsc-dataseed.binance.org/
PRIVATE_KEY=9834cdf969819c5ce1099dc496544c956c80b7ffd073f07cb197763767957d36
WALLET_ADDRESS=0xc919a4c28ec02e698c5184d67a73217b4abcc52c
PANCAKE_ROUTER=0x10ED43C718714eb63d5aA57B78B54704E256024E #PANCAKE ROUTE
AMOUNT_TO_BUY=0.05 #Amount to buy
MIN_TX_AMOUNT=50000  # Minimum value (USD) of a whale transaction for the bot to track
SLIPPAGE=5  # Price slippage (in %) when buying tokens
PROFIT_TARGET=5  # Profit target percentage to take profit (105%)
STOP_LOSS=5  # Stop-loss percentage if the price drops (95%)
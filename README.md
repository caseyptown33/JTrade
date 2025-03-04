🚀 AutoTrade Bot on Free VPS

A bot that listens for whale swap transactions and automatically buys tokens before selling them at a higher price. It runs on a free VPS and supports Binance Smart Chain (BSC) using PancakeSwap.

📌 How It Works

✅The bot continuously monitors swap transactions on the blockchain.

✅When a whale (large trader) swaps tokens exceeding a predefined USD amount, the bot quickly buys the token.

✅The bot waits for a price increase and sells at a target profit or cuts losses using stop-loss.

✅Transactions are executed using PancakeSwap's Router contract.

📋 Installation Guide

1️⃣ Install Python

Ensure Python is installed on your VPS. If not, install it:

sudo apt update && sudo apt install python3 python3-pip -y

2️⃣ Install Required Dependencies

pip install web3 python-dotenv requests

3️⃣ Configure Your .env File

Create a .env file in the same directory as the bot and edit it with your credentials:

SC_NODE_URL=https://bsc-dataseed.binance.org/
PRIVATE_KEY=YOUR_METAMASK_PRIVATE_KEY
WALLET_ADDRESS=YOUR_METAMASK_WALLET_ADDRESS
PANCAKE_ROUTER=0x10ED43C718714eb63d5aA57B78B54704E256024E
AMOUNT_TO_BUY=0.05  # Amount of BNB to spend per trade
MIN_TX_AMOUNT=50000  # Minimum whale transaction value in USD
SLIPPAGE=5  # Maximum price slippage (in %)
PROFIT_TARGET=5  # Sell when profit reaches 5%
STOP_LOSS=5  # Sell if the price drops 5%

🔍 Explanation of .env File

SC_NODE_URL: The blockchain node to connect to.

PRIVATE_KEY: Your MetaMask private key (⚠️ Keep this secret!).

WALLET_ADDRESS: Your MetaMask wallet address.

PANCAKE_ROUTER: The PancakeSwap router address for swapping.

AMOUNT_TO_BUY: The amount of BNB to use per trade.

MIN_TX_AMOUNT: The minimum transaction value (in USD) for tracking whales.

SLIPPAGE: The allowed slippage in percentage.

PROFIT_TARGET: The percentage gain at which to sell.

STOP_LOSS: The percentage loss at which to sell.

▶️ Run the Bot

After setting up, start the bot with:

python JTrade.py

⚠️ Important Notes

Test with a small amount first (e.g., 0.1 BNB + gas fees).

Use a secure VPS to protect your private key.

This bot does not guarantee profits. Trade at your own risk.

🎯 Conclusion

This bot automates trading based on whale transactions, aiming to take advantage of price spikes. Adjust the .env settings according to your risk tolerance and trading strategy.

🚀 Happy Trading!


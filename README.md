AutoTrade Bot on Free VPS

Introduction

This AutoTrade bot listens for whale swap transactions on the Binance Smart Chain (BSC) and executes trades automatically. The bot aims to buy tokens before a price surge and sell them at a higher price for profit.

How It Works

The bot continuously monitors BSC transactions, specifically swap transactions on PancakeSwap.

When a whale transaction exceeds a defined threshold (e.g., $50,000 USD), the bot identifies the token being purchased.

If the token meets predefined conditions, the bot automatically buys a specified amount.

The bot monitors the token price and sells when the profit target is reached or exits when the stop-loss threshold is hit.

Installation Guide

1. Install Python

Ensure you have Python installed on your system. You can download it from Python's official website.

2. Install Required Dependencies

Run the following command to install necessary libraries:

pip install web3 python-dotenv requests

3. Configure the .env File

The bot uses a .env file for storing private credentials and trading parameters. The file should be in the root directory of the bot.

Example .env Configuration:

SC_NODE_URL=https://bsc-dataseed.binance.org/
PRIVATE_KEY=YOUR_METAMASK_PRIVATE_KEY
WALLET_ADDRESS=YOUR_METAMASK_WALLET_ADDRESS
PANCAKE_ROUTER=0x10ED43C718714eb63d5aA57B78B54704E256024E # PancakeSwap Router Address
AMOUNT_TO_BUY=0.05  # Amount of BNB to use for each trade
MIN_TX_AMOUNT=50000  # Minimum whale transaction value in USD to trigger the bot
SLIPPAGE=5  # Slippage percentage (e.g., 5%)
PROFIT_TARGET=5  # Profit-taking percentage (e.g., sell at 105% of buy price)
STOP_LOSS=5  # Stop-loss percentage (e.g., exit if price drops to 95%)

4. Explanation of .env Parameters:

SC_NODE_URL: BSC node URL (default: Binance RPC)

PRIVATE_KEY: Your MetaMask private key (⚠️ Keep this secure, never share it!)

WALLET_ADDRESS: Your public wallet address (used for transactions)

PANCAKE_ROUTER: PancakeSwap's router contract address (used for executing swaps)

AMOUNT_TO_BUY: Amount of BNB used for each trade

MIN_TX_AMOUNT: The minimum whale transaction value in USD to trigger a trade

SLIPPAGE: Allowed slippage percentage to prevent failed trades

PROFIT_TARGET: The percentage at which the bot sells to secure profits

STOP_LOSS: The percentage at which the bot exits a position to limit losses

5. Running the Bot

Once configured, run the bot with:

python run.py

6. Testing with a Small Amount

To ensure the bot works correctly, start by setting AMOUNT_TO_BUY=0.1 BNB and monitoring its behavior before increasing the investment amount.

Final Notes

Always test with a small amount before increasing trade volume.

The bot requires a small amount of BNB for gas fees.

Use at your own risk; trading involves financial risks.

🚀 Happy Trading! 🚀


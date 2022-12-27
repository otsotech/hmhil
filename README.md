# How Much Have I Lost
A simple script to check the current value of a cryptocurrency and compare it to the amount invested, displaying the profit or loss.

## Features
- Shows current value of cryptocurrency
- Shows profit or loss compared to investment
- Shows percentage increase or decrease in value since the program was started
## Requirements
- Python 3
- requests library
- clint library
- configparser library
## Usage
1. Clone the repository
2. Install the required libraries by running pip install -r requirements.txt in the project directory
3. Edit config.ini in the project directory with the following format:
```
[hmhil]

# Crypto
crypto: [e.g. BTC, ETH]

# Currency
currency: [e.g. EUR, USD]

# Crypto amount
crypto_amount: [e.g. 1.25]

# Total investment
investment: [e.g. 100]
```
5. Run the script with the run.bat file

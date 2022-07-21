# imports
import requests
import os
import time
import configparser
from os import system
from distutils.command.config import config
from clint.textui import colored

config = configparser.ConfigParser()
config.read("config.ini")
crypto = config.get("hmhil", "crypto")
currency = config.get("hmhil", "currency")
cryptoamount = config.get("hmhil", "crypto_amount")
investment = config.get("hmhil", "investment")
clear = lambda: os.system('cls')
line=(colored.yellow('\n' + '─' * 60 + '\n'))
key='https://api.binance.com/api/v3/ticker/price?symbol='+crypto+currency # get data from Binance
data = requests.get(key)
data = data.json()
crypto=str(crypto)
currency=str(currency)
cryptoamount=float(cryptoamount)
investment=float(investment)
sincevalue=float(float(f"{data['price']}"))
system("title " + "How Much Have I Lost")

 # loop
while (0==0):

    # get crypto value
    data = requests.get(key)
    data = data.json()
    cryptovalue=float(f"{data['price']}")

    clear() # clear / refresh

    # credit
    print('Github: https://github.com/otsoniemi\nTwitter: https://twitter.com/otsoniemitech')

    print(line)

    # static data
    print('Crypto amount:\n    ' + str(cryptoamount) + ' ' + crypto + '\n')
    print('Investment:\n    ' + str(investment) + ' ' + currency)
    print(line)

    # dynamic data
    print(crypto + ' value:\n    ' + str(cryptovalue) + ' ' + currency)
    print(line)

    # loss/profit amount
    if cryptovalue*cryptoamount-investment<0:
        print('Loss:\n    ' + str(colored.red(round(cryptovalue*cryptoamount-investment,2))) + ' ' + currency)
    else:
        print('Profit:\n    ' + str(colored.green(round(cryptovalue*cryptoamount-investment,2))) + ' ' + currency)

    print(line)

    # profit increase/decrease percentage 
    if(sincevalue<cryptovalue):
        print('Since program was opened:')
        print('    ' + crypto + ' value was: ' + str(sincevalue) + ' ' + crypto)
        print('    ' + crypto + ' value has increased: ' + str(colored.green(round(cryptovalue-sincevalue,2))) + ' ' + currency)
        print('    ' + crypto + ' value has increased: ' + str(colored.green(round(100-(100*sincevalue/(cryptovalue)),2))) + ' %')
    elif(sincevalue>cryptovalue):
        print('Since program was opened:')
        print('    ' + crypto + ' value was: ' + str(sincevalue) + ' ' + crypto)
        print('    ' + crypto + ' value has decreased: ' + str(colored.red(round(sincevalue-cryptovalue,2))) + ' ' + currency)
        print('    ' + crypto + ' value has decreased: ' + str(colored.red(round(100*(sincevalue/(cryptovalue))-100,2))) + ' %')
    else:
        print('Since program was opened:')
        print('    ' + crypto + ' value has stayed the same.')
        print('    ' + crypto + ' value has stayed the same.')
        print('    ' + crypto + ' value was: ' + str(sincevalue) + ' ' + crypto)
    
    time.sleep(1) # wait a second before refresh

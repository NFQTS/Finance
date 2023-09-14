#import requests
import json
import random
import os

POLYGON_API = os.environ["polygon_api"]
SOLANA_API = os.environ["solana_api"]
ETHEREUM_API = os.environ["eth_api"]
BITCOIN_API = os.environ["btc_api"]

def scan_crypto_prices(coin):
    """ Scans for updated crypto prices and saves the relevant data."""
    if coin == "Matic":
        matic_price = get_matic_price()
        matic_market_cap = get_matic_market_cap()
        print(f"Matic price: {matic_price}")
        print(f"Matic price: {matic_market_cap}")
    elif coin == "Sol":
        pass
    elif coin == "Eth":
        pass
    elif coin == "Btc":
        pass
    else:
        print("Error wrong coin entered or something.")

def get_matic_price():
    url = f"https://api.polygonscan.com/api?module=stats&action=maticprice&apikey={POLYGON_API}"
    matic_price = 1
    return matic_price

def get_matic_market_cap(price):
    url = f"https://api.polygonscan.com/api?module=stats&action=maticsupply&apikey={POLYGON_API}"
    matic_market_cap = url_result * price
    return matic_market_cap

def get_sol_price():
    url = f"https://api.polygonscan.com/api?module=stats&action=maticprice&apikey={POLYGON_API}"
    matic_price = 1
    return matic_price

def get_sol_market_cap(price):
    url = f"https://api.polygonscan.com/api?module=stats&action=maticsupply&apikey={POLYGON_API}"
    matic_market_cap = url_result * price
    return matic_market_cap
    
def paper_training():
    """ Tests the current model in a simulated real life environment to compare performance."""
    pass

def build_arb_model():
    """ Builds a new arbitrage model to test."""
    pass

def optimize_neural_network():
    pass

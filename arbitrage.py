#import requests
import json
import random
import os

# POLYGON_API = os.environ["polygon_api"]
# SOLANA_API = os.environ["solana_api"]
# ETHEREUM_API = os.environ["eth_api"]
# BITCOIN_API = os.environ["btc_api"]
crypto_tokens = ["Matic", "Sol", "Eth", "Btc"]
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
    
def paper_training(asset_type):
    """ Tests the current model in a simulated real life environment to compare performance."""
    pass

def build_arb_model():
    """ Builds a new arbitrage model to test. Should test exchange-based arbitrage, triangular arbitrage (USD -> ETH -> BTC), and variations of hybrids."""
    
    # Check for previous data to try to inherit working methods.
    # Want to test models against each other in ways that can help us reverse engineer performance increases.
    # 4 layered approach for now:
    # 1.) Best performing model
    # 2.) Challenger
    # 3.) Brand new random one
    # 4.) Experimental one that is trying to outperform the others.
    # Worst performer gets dropped
    # Models are tested and mutated in a variety of time frames
    # 10 epochs, 100 epochs, 1000 epochs, 10000 epochs. Each with different tests and mutation schedules.
    pass

def arbitrage_crypto(coin_type):
    pass

def arbitrage_fiat(type):
    pass
    
def optimize_neural_network():
    pass

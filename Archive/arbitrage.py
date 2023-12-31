### Deprecated for now.

# import requests
# import json
# import random
# import os

# # Initialize the POLYGON_API variable if you plan to use it.
# POLYGON_API = os.environ["polygon_api"]
# # SOLANA_API = os.environ["solana_api"]
# # ETHEREUM_API = os.environ["eth_api"]
# # BITCOIN_API = os.environ["btc_api"]
# # crypto_tokens = ["Matic", "Sol", "Eth", "Btc"]
# # ml_tools = ["tensorflow", "keras", "skLearn", "pytorch"]
# crypto_tokens = ["Matic"]
# ml_tools = ["tensorflow"]
# current_best_models = []

# class arb_batch():
#     """ An object consisting of arbitrage models to use for trading assets."""
    
#     def __init__(self, tokens, tools):
#         self.models = {"Crypto": {}}
#         for tool in tools:
#             self.models["Crypto"][tool] = {}  # Create a dictionary for each ML tool
#             for token in tokens:
#                 self.models["Crypto"][tool][token] = {"Best": None, "Challenger": None, "Test": None, "Control": None}


# def scan_crypto_prices(coin):
#     """ Scans for updated crypto prices and saves the relevant data."""
#     if coin == "Matic":
#         matic_price = get_matic_price()
#         matic_market_cap = get_matic_market_cap()
#         print(f"Matic price: {matic_price}")
#         print(f"Matic market cap: {matic_market_cap}")

#     else:
#         print("Error wrong coin entered or something.")

# def get_matic_price():
#     url = f"https://api.polygonscan.com/api?module=stats&action=maticprice&apikey={POLYGON_API}"
    
#     try:
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             data = response.json()
#             print(data)
#             matic_price = data['result']['maticusd']
            
#             if matic_price is not None:
#                 return float(matic_price)
#             else:
#                 print("Error: Matic price data not found in the response.")
#                 return None
#         else:
#             print("Error: Unable to retrieve Matic price data.")
#             return None

#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return None

# def get_matic_supply():
#     url = f"https://api.polygonscan.com/api?module=stats&action=maticsupply&apikey={POLYGON_API}"
    
#     try:
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             data = response.json()
#             print(data)
#             matic_supply = data['result']
            
#             if matic_supply is not None:
#                 return int(matic_supply)
#             else:
#                 print("Error: Matic price data not found in the response.")
#                 return None
#         else:
#             print("Error: Unable to retrieve Matic price data.")
#             return None

#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return None

# def build_arb_batch(asset_lists, ml_tool_list):
#     """ Builds arbitrage model batches to test. Should test exchange-based arbitrage, triangular arbitrage (USD -> ETH -> BTC), and variations of hybrids."""
#     print("Need to check for a list of existing models to build/test against.")
#     if len(current_best_models) == 0:
#         new_batch = arb_batch(asset_lists, ml_tool_list)
#         #print(new_batch.models)
#         print("Blank batch created, populating models for each asset.")
#     for tool in ml_tools:
#         for asset in new_batch.models:
#             for token in new_batch.models[asset][tool]:
#                 for model in new_batch.models[asset][tool][token]:
#                     if new_batch.models[asset][tool][token][model] is not None:
#                         print("model exists")
#                     else:
#                         print("Can't have empty models, need to create random models to begin.")
#                         print(f"{token} {tool} Model:", new_batch.models[asset][tool][token])
#                         new_model = generate_new_model(tool, token)
#                         new_batch.models[asset][tool][token][model] = new_model
#     print(new_batch.models)
#     # Check for previous data to try to inherit working methods.
#     # Want to test models against each other in ways that can help us reverse engineer performance increases.
#     # 4 layered approach for now:
#     # 1.) Best-performing model
#     # 2.) Challenger
#     # 3.) Brand new random one
#     # 4.) Experimental one that is trying to outperform the others.
#     # Worst performer gets dropped
#     # Models are tested and mutated in a variety of time frames
#     # 10 epochs, 100 epochs, 1000 epochs, 10000 epochs. Each with different tests and mutation schedules.
#     # Will probably do batches to reduce errors/ remove crazy rng.

# def generate_new_model(ml_tool, coin):
#     """ Generates a new neural network arbitrage model and saves it to the arb batch."""
#     # Not entirely sure how to finish this...
#     # May use an evolutionary style cnn that can pass on traits/mutations, and use randomness to retry different evolutionary paths...
#     print(f"Generating {ml_tool} {coin} model.")
#     new_model = 1
#     return new_model

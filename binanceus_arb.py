import ccxt
import time
import json

# Define the cryptocurrency pairs you want to monitor
pairs = ['BTC/USDT', 'BTC/USDC']
wallet_total = {"USDT": 100, "USDC": 100, "BTC": 0.0002}
risk_percentage = 0.005

# Define criteria for data management
MAX_RUNTIME_SECONDS = 60  # Maximum runtime in seconds (1 hour)
order_depth = 15
def load_exchange_orders():
    try:
        with open('exchange_order_data.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

# Dictionary to store exchange order book data with timestamps for different pairs
exchange_order_dict = load_exchange_orders()
highest_arb_opp = 0


# Function to save exchange orders to JSON
def save_exchange_orders():
    # Serialize the exchange_order_dict to JSON and write it to a file
    with open('exchange_order_data.json', 'w') as json_file:
        json.dump(exchange_order_dict, json_file, indent=4)
    print("Exchange order data saved to 'exchange_order_data.json'.")

def detect_arbitrage_opportunity(pair):
    try:
        # Fetch order book data
        exchange_binanceus = ccxt.binanceus()
        order_book = exchange_binanceus.fetch_order_book(pair)
        store_exchange_orders(exchange_binanceus.id, order_book, pair)
        #print(order_book)
        # Calculate potential profit percentage
        bid_price = order_book['bids'][1][0]
        ask_price = order_book['asks'][1][0]
        profit_percentage = ((ask_price - bid_price) / bid_price) * 100

        if profit_percentage > 0.1:  # Arbitrage opportunity threshold
            # Print arbitrage opportunity details
            print(f"Arbitrage Opportunity Detected for {pair} on {exchange_binanceus.id}!")
            print(f"Buy {pair} at {bid_price}")
            print(f"Sell {pair} at {ask_price}")
            print(f"Potential Profit Percentage: {profit_percentage:.2f}%\n")

            # Check if this opportunity has the highest profit potential
            global highest_arb_opp
            if profit_percentage > highest_arb_opp:
                highest_arb_opp = profit_percentage
                print(f"Highest Profit Percentage Updated: {highest_arb_opp:.2f}%\n")

    except Exception as e:
        print(f"Error: {str(e)}")

def store_exchange_orders(exchange, data, asset_pair):
    print(f"Storing {exchange} order book data for {asset_pair}")
    exchange_str = str(exchange)

    # If the exchange is not in the dictionary, create a new entry
    if exchange_str not in exchange_order_dict:
        exchange_order_dict[exchange_str] = {}

    # If the pair is not in the exchange's entry, create a list to store data
    if asset_pair not in exchange_order_dict[exchange_str]:
        exchange_order_dict[exchange_str][asset_pair] = []

    # Extract the first 15 bids and asks
    bids = data['bids'][:order_depth]
    asks = data['asks'][:order_depth]

    # Store the order book data for the specific pair along with a timestamp
    timestamp = int(time.time())  # Get the current Unix timestamp
    exchange_order_dict[exchange_str][asset_pair].append({
        timestamp: {
            'bids': bids,
            'asks': asks
        }
    })

    print("Records updated.")
    save_exchange_orders()
# Main loop
run = True
while run:
    start_time = time.time()
    # Check for arbitrage opportunities for each pair
    for pair in pairs:
        detect_arbitrage_opportunity(pair)

    # Check the runtime
    current_time = time.time()
    runtime = current_time - start_time
    print("Runtime", runtime)
    if current_time - start_time >= MAX_RUNTIME_SECONDS:
        print(f"Maximum runtime ({MAX_RUNTIME_SECONDS} seconds) reached. Exiting.")
        break

    print(f"Highest Profit Percentage Found: {highest_arb_opp:.2f}%")
    print("Sleeping for a few seconds to give the market time to move.")
    time.sleep(5)

trading_rules = {
    "profit_threshold": .25,
    "loss_tolerance": risk_percentage,
    "base_bet_USDT": 100
}


# Need to make a way for reinforcement learning agents to compete for profits.
# Need a way for an RNN to analyze order book bid and ask data to look for patterns.
# Need a way for RNN powered reinforcement learning agents to optimize the rest of the system.


# Decision points:
# Which crypto
# Which exchange
# Which time periods
# Which price to buy/sell
# What data do we go off of
# Which type of ML models do we use
# How do we adjust the weights and biases
# What type of activation functions do we use
# What part of the data set do we use
# How to predict fees

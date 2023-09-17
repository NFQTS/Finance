import ccxt
import time

# Initialize the Binance US exchange object
exchange_binanceus = ccxt.binanceus()

# Define the cryptocurrency pairs you want to monitor
pairs = ['BTC/USDT', 'BTC/USDC']

# Dictionary to store exchange order book data with timestamps for different pairs
exchange_order_dict = {}

def store_exchange_orders(exchange, data, asset_pair):
    print(f"Storing {exchange} order book data for {asset_pair}")
    exchange_str = str(exchange)

    # If the exchange is not in the dictionary, create a new entry
    if exchange_str not in exchange_order_dict:
        exchange_order_dict[exchange_str] = {}

    # Store the order book data for the specific pair along with a timestamp
    timestamp = int(time.time())  # Get the current Unix timestamp
    exchange_order_dict[exchange_str][asset_pair] = {
        'timestamp': timestamp,
        'order_book_data': data
    }

    print("Records updated.")

def detect_arbitrage_opportunity(exchange, pair):
    try:
        # Fetch order book data
        order_book = exchange.fetch_order_book(pair)
        store_exchange_orders(exchange.id, order_book, pair)

        # Extract best bid and ask prices
        bid_price = order_book['bids'][0][0]
        ask_price = order_book['asks'][0][0]

        # Calculate potential profit percentage
        profit_percentage = ((ask_price - bid_price) / bid_price) * 100

        if profit_percentage > 0:  # Arbitrage opportunity threshold
            # Print arbitrage opportunity details
            print(f"Arbitrage Opportunity Detected for {pair} on {exchange.id}!")
            print(f"Buy {pair} at {bid_price}")
            print(f"Sell {pair} at {ask_price}")
            print(f"Potential Profit Percentage: {profit_percentage:.2f}%\n")

    except Exception as e:
        print(f"Error: {str(e)}")
run = True
while run:
    # Check for arbitrage opportunities for each pair
    for pair in pairs:
        detect_arbitrage_opportunity(exchange_binanceus, pair)
    
    # Print the stored order book data with timestamps
    print(exchange_order_dict)
    print("Sleeping for 3 minutes to give the market time to move.")
    time.sleep(180)

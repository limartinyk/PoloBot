import requests
import csv
import threading

#initializing csv
with open("historical_data.csv", 'a', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['time', 'price', 'size', 'bid', 'ask', 'volume'])

# writing to csv
def writedata():
	threading.Timer(1.0, writedata).start()
	with open("historical_data.csv", 'a', newline='') as csvfile:
		writer = csv.writer(csvfile)
		ticker_payload = requests.get("https://api.gdax.com/products/BTC-USD/ticker").json()

		price_dict = dict()
		size_dict = dict()
		bid_dict = dict()
		ask_dict = dict()
		volume_dict = dict()
		time = set()

		p_data = ticker_payload['price']
		s_data = ticker_payload['size']
		b_data = ticker_payload['bid']
		a_data = ticker_payload['ask']
		v_data = ticker_payload['volume']
		time_data = ticker_payload['time']

		price_dict[time_data] = p_data
		size_dict[time_data] = s_data
		bid_dict[time_data] = b_data
		ask_dict[time_data] = a_data
		volume_dict[time_data] = v_data
		time.add(time_data)

		for k in sorted(time):
			row = [k, price_dict[k], size_dict[k], bid_dict[k], ask_dict[k], volume_dict[k]]
			print(row)
			writer.writerow(row)
writedata()

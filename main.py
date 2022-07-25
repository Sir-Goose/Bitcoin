import json
import sys

import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    count = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
json_data = json.loads(response.text)
btc_price = json_data['bpi']['USD']['rate']

btc_price = btc_price.replace(',', '')

btc_price = float(btc_price) * float(sys.argv[1])

#btc_price = '$' + str(btc_price)
print(f"${btc_price:,.4f}")

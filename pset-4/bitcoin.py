import requests
import sys

if len(sys.argv) == 2:
    try:
        coins_count = float(sys.argv[1])

        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            json_response = response.json()
            price = json_response['bpi']['USD']['rate_float'] * coins_count
            print(f"${price:,.4f}")
        except requests.RequestException:
            sys.exit('Request error!')
    except:
        sys.exit('Command-line argument is not a number')
else:
    sys.exit('Missing command-line argument')
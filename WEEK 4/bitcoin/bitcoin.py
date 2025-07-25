import requests
import sys

api_key = "API_KEY"
api_url = f"https://rest.coincap.io/v2/assets/bitcoin?apiKey={api_key}"

if len(sys.argv) == 2:
  try:
   n =  float(sys.argv[1])
  except ValueError:
    sys.exit("Invalid Number!")
else:
  sys.exit("Missing command-line argument")

try:
  response = requests.get(api_url)
  final_response = response.json()
  price = float(final_response["data"]["priceUsd"])
  total_cost = n * price
  print(f"${total_cost:,.4f}")
except requests.RequestException:
  sys.exit("Error fetching data")




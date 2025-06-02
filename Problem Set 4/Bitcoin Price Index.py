import sys
import requests
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument must be a number")
    try:
        api_key = "YourApiKey"  # Replace this with your real API key from CoinCap
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
        total = bitcoins * price
        print(f"${total:,.4f}")
    except requests.RequestException:
        sys.exit("Network error: Could not retrieve Bitcoin price")
    except (KeyError, TypeError, ValueError):
        sys.exit("Error: Unexpected response from API")
if __name__ == "__main__":
    main()

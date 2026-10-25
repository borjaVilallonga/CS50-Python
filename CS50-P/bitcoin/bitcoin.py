import sys
import requests

def main():
    try:
        bitcoins = float(sys.argv[1])
    except (IndexError, ValueError):
        sys.exit("Missing command-line argument")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=d4a194b9bf0114bb9fcc62fa80932e6c6bea697e261ad07f76f45ad34aa38eba")
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Request failed")

    total = bitcoins * price
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()

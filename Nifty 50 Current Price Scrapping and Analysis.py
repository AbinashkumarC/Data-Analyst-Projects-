import requests
from bs4 import BeautifulSoup
import time

def priceTracker():
    try:
        live_link = 'https://finance.yahoo.com/quote/%5ENSEI/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(live_link, headers=headers)
        response.raise_for_status()  # Check for request errors
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Replace with the correct tag and attribute/class name for the price element
        price_element = soup.find('fin-streamer', {"data-field": "regularMarketPrice"})
        if price_element:
            Price = price_element.text
            return Price
        else:
            return "Price element not found"
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"
    except Exception as e:
        return f"Error: {e}"

while True:
    print('Current price of Nifty 50: ' + priceTracker())
    time.sleep(10)  # Wait for 60 seconds before the next request

import requests
from bs4 import BeautifulSoup

# Define the URL of the TradingView page
url = "https://cn.tradingview.com/chart/r5lnT6rw/"

# Define a user-agent header to mimic a web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Send an HTTP GET request to the URL with headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the canvas element with the specified aria-label attribute
    canvas_element = soup.find('canvas', {'aria-label': True})

    # Extract the aria-label attribute
    aria_label = canvas_element['aria-label']

    # Print the extracted aria-label
    print("Aria Label:", aria_label)
else:
    print("Failed to retrieve the page. Status code:", response.status_code)

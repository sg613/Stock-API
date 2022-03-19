from flask import Flask,jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return "Thanks for checking out my Stock API! Instructions are in the documentation here: "

@app.route('/<ticker>')
def getStock(ticker):
    try:
        baseUrl = 'https://www.marketwatch.com/investing/fund/'
        url = baseUrl + ticker
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        price = soup.find("meta", {"name": "price"})['content']
        change = soup.find("meta", {"name": "priceChange"})['content']
        percent = soup.find("meta", {"name": "priceChangePercent"})['content']
        return jsonify({'price': price, '$ Change': change, 'percent': percent})
    except:
        return "Ticker not Found"

@app.route('/<ticker>/price')
def stockPrice(ticker):
    try:
        baseUrl = 'https://www.marketwatch.com/investing/fund/'
        url = baseUrl + ticker
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        price = soup.find("meta", {"name": "price"})['content']
        return jsonify({'price': price})
    except:
        return "Ticker not Found"

@app.route('/<ticker>/change')
def stockChange(ticker):
    try:
        baseUrl = 'https://www.marketwatch.com/investing/fund/'
        url = baseUrl + ticker
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        change = soup.find("meta", {"name": "priceChange"})['content']
        return jsonify({'$ Change': change})
    except:
        return "Ticker not Found"
    
@app.route('/<ticker>/percent')
def stockPercent(ticker):
    try:
        baseUrl = 'https://www.marketwatch.com/investing/fund/'
        url = baseUrl + ticker
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        percent = soup.find("meta", {"name": "priceChangePercent"})['content']
        return jsonify({'Percent Change': percent})
    except:
        return "Ticker not Found"
    


if __name__ == "__main__":
    app.run(debug=True)
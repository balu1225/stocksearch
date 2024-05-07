from flask import Flask, jsonify, request, render_template
import requests
import logging
from datetime import datetime
# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# API Key and Base URL for Tiingo
API_KEY = 'e02ffcf8c4bb38207f3acd04d9574bcf5522f91e'
TIINGO_DAILY_API_URL = 'https://api.tiingo.com/tiingo/daily/'
TIINGO_IEX_API_URL = 'https://api.tiingo.com/iex/'
TIINGO_PRICES_API_URL = 'https://api.tiingo.com/iex/'  # Using IEX base URL for prices

# Home route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Route to fetch data from Tiingo Daily API for a specific ticker
@app.route('/api/tiingo/<ticker>', methods=['GET'])
def get_tiingo_data(ticker):
    url = f'{TIINGO_DAILY_API_URL}{ticker}'
    params = {'token': API_KEY}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        logging.error(f"Failed to fetch data from Tiingo Daily API for ticker {ticker}: {response.text}")
        return jsonify({'error': 'Failed to fetch data from the Tiingo API', 
                        'status_code': response.status_code, 
                        'message': response.text}), 500

# Route to fetch real-time data from Tiingo IEX API for a specific ticker
@app.route('/api/iex/<ticker>', methods=['GET'])
def get_iex_data(ticker):
    params = {
        'tickers': ticker,
        'token': API_KEY
    }
    response = requests.get(TIINGO_IEX_API_URL, params=params)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        logging.error(f"Failed to fetch data from Tiingo IEX API for ticker {ticker}: {response.text}")
        return jsonify({'error': 'Failed to fetch data from the IEX API', 
                        'status_code': response.status_code, 
                        'message': response.text}), 500

# Route to fetch historical stock prices with resampling
@app.route('/api/prices/<ticker>', methods=['GET'])
def get_prices_data(ticker):
    startDate = request.args.get('startDate', '2019-01-02')
    resampleFreq = request.args.get('resampleFreq', '5min')
    columns = request.args.get('columns', 'close')
    
    params = {
        'startDate': startDate,
        'resampleFreq': resampleFreq,
        'columns': columns,
        'token': API_KEY
    }
    response = requests.get(f'{TIINGO_PRICES_API_URL}{ticker}/prices', params=params)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        logging.error(f"Failed to fetch historical price data for ticker {ticker}: {response.text}")
        return jsonify({'error': 'Failed to fetch historical price data',
                        'status_code': response.status_code,
                        'message': response.text}), 500


def format_date(date_string):
    # Parse the date string and format it
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
        formatted_date = date_object.strftime('%B %d, %Y')
    except ValueError:
        formatted_date = date_string  # Return the original string if parsing fails
    return formatted_date

# Route to fetch news articles related to a specific ticker from News API
@app.route('/api/news/<ticker>', methods=['GET'])
def get_news_data(ticker):
    NEWS_API_URL = 'https://newsapi.org/v2/everything'
    NEWS_API_KEY = '0482bfd9125543169f5589e19e0d6de8'
    
    params = {
        'q': ticker,
        'apiKey': NEWS_API_KEY
    }
    response = requests.get(NEWS_API_URL, params=params)
    
    if response.status_code == 200:
        news_data = response.json()['articles']
        formatted_news = []
        for article in news_data:
            formatted_article = {
                'title': article['title'],
                'date': format_date(article['publishedAt']),  # Format the date
                'image': article['urlToImage'],
                'link': article['url']
            }
            formatted_news.append(formatted_article)
        
        return jsonify(formatted_news)
    else:
        logging.error(f"Failed to fetch news data for ticker {ticker}: {response.text}")
        return jsonify({'error': 'Failed to fetch news data', 
                        'status_code': response.status_code, 
                        'message': response.text}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

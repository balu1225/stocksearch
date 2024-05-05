from flask import Flask, jsonify, request, render_template
import requests
import logging

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
    columns = request.args.get('columns', 'open,high,low,close,volume')
    
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

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify, request ,render_template
import requests

app = Flask(__name__)

API_KEY = 'e02ffcf8c4bb38207f3acd04d9574bcf5522f91e'
TIINGO_API_URL = 'https://api.tiingo.com/tiingo/daily/'
IEX_API_URL = 'https://api.tiingo.com/iex/'

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/tiingo')
def get_tiingo_data():
    ticker = 'aapl'
    url = f'{TIINGO_API_URL}{ticker}'
    params = {'token': API_KEY}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data from the Tiingo API', 'status_code': response.status_code}), 500

@app.route('/iex')
def get_iex_data():
    params = {
        'tickers': 'aapl',
        'token': API_KEY
    }
    response = requests.get(IEX_API_URL, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data from the IEX API', 'status_code': response.status_code}), 500

if __name__ == '__main__':
    app.run(debug=True)

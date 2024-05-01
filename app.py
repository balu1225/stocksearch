from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/tiingo/aapl', methods=['GET'])
def get_data():
    headers = {'Content-Type': 'application/json'}
      # Replace with your Tiingo token
    url = f"https://api.tiingo.com/tiingo/daily/aapl?token=e02ffcf8c4bb38207f3acd04d9574bcf5522f91e"
    
    # Make the request to Tiingo API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response from Tiingo
        return jsonify(response.json())
    else:
        # Return an error message if the request failed
        return jsonify({'error': 'Failed to fetch data from Tiingo'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

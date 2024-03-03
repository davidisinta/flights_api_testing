from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

RAPIDAPI_KEY = "e2262991e2mshd620a6a0d79a320p19181djsn46bab34a1096"
RAPIDAPI_HOST = "tripadvisor16.p.rapidapi.com"
FLIGHTS_URL = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"


def get_flight_data():
    query_params = {
        "sourceAirportCode": "BOM",
        "destinationAirportCode": "DEL",
        "date": "2024-04-22",
        "itineraryType": "ONE_WAY",
        "sortOrder": "PRICE",
        "numAdults": "1",
        "numSeniors": "0",
        "classOfService": "ECONOMY",
        "pageNumber": "1",
        "currencyCode": "USD"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    response = requests.get(FLIGHTS_URL, headers=headers, params=query_params)
    return response.json()


@app.route('/')
def index():
    flight_data = get_flight_data()
    print(flight_data)
    return render_template('index.html', flight_data=flight_data)


@app.route('/api/flights')
def api_flights():
    flight_data = get_flight_data()
    return jsonify(flight_data)


if __name__ == '__main__':
    app.run()

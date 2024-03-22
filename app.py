from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

RAPIDAPI_KEY = "e2262991e2mshd620a6a0d79a320p19181djsn46bab34a1096"
RAPIDAPI_HOST = "tripadvisor16.p.rapidapi.com"
FLIGHTS_URL = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"

def get_flight_data(payload):
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    response = requests.get(FLIGHTS_URL, headers=headers, params=payload)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')

    if request.method == 'POST':
        flight_date = request.form['date']
        print(flight_date)
        itinerary_type = request.form['itineraryType']
        print(itinerary_type)

        payload = {
            "sourceAirportCode": "BOM",
            "destinationAirportCode": "DEL",
            "date": flight_date,
            "itineraryType": itinerary_type,
            "sortOrder": "PRICE",
            "numAdults": "1",
            "numSeniors": "0",
            "classOfService": "ECONOMY",
            "pageNumber": "1",
            "currencyCode": "USD",
            "nonstop":"yes"
        }

        flight_data = get_flight_data(payload)
        print(flight_data)
        return render_template("flights.html", response_json=flight_data)

@app.route('/api/flights')
def api_flights():
    params = {
        "sourceAirportCode": "BOM",
        "destinationAirportCode": "DEL",
        "date": "2024-11-11",
        "itineraryType": "ROUND_TRIP",
        "sortOrder": "PRICE",
        "numAdults": "1",
        "numSeniors": "0",
        "classOfService": "ECONOMY",
        "pageNumber": "1",
        "currencyCode" : "USD",
    }
    flight_data = get_flight_data(params)
    print(flight_data)
    return jsonify(flight_data)

if __name__ == '__main__':
    app.run(debug=True,port = 5677)

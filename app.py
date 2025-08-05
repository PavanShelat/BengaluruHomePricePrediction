from flask import Flask, request, jsonify
import util
import os

app = Flask(__name__, static_url_path="", static_folder="client")  # Point to your HTML folder

@app.route('/')
def index():
    return app.send_static_file('app.html')  # Serve the homepage

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])  # POST only, not GET
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets this
    app.run(host="0.0.0.0", port=port)


from flask import Flask, render_template, request
import requests
import joblib

app = Flask(__name__)

model = joblib.load("weather_model.pkl")

API_KEY = "ad89b9eeb4d04c25a6664746262204"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    prediction = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"
        data = requests.get(url).json()

        if "current" in data:
            temp = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]

            prediction = model.predict([[temp]])[0]

            weather = {
                "city": city,
                "temp": temp,
                "condition": condition
            }

    return render_template("index.html", weather=weather, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
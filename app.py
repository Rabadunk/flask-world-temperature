from flask import Flask, render_template, request
#Importing requests to request from url
import requests
import weather



app = Flask(__name__)

@app.route('/response', methods=['POST'])
def temperature():
    city = request.form['city']
    weather_dict = weather.weatherData(city)
    dates = weather_dict['dates']
    days = weather.days(dates)
    magical_length = len(days)
    return render_template('index.html', length = magical_length, days = days, dates = dates, weather_dict = weather_dict)

@app.route('/')
def index():
    weather_dict = weather.weatherData('auckland')
    dates = weather_dict['dates']
    days = weather.days(dates)
    magical_length = len(days)
    return render_template('index.html', length = magical_length, days = days, dates = dates, weather_dict = weather_dict)


if __name__ == '__main__':
    app.run(debug=True)

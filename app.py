from flask import Flask, render_template, request
#Importing requests to request from url
import requests

#Importing ast to convert str to dict
import ast
f = open("countries.txt", "r")
data = f.read()
countries = ast.literal_eval(data)
f.close

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    city = request.form['city']
    country = request.form['country']
    countryCode = countries[country]
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city + ',' + countryCode + '&appid=0cd5498b4fc08eb51125e83318e058ef')
    json_object = response.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = round(temp_k - 273.15, 2)
    return render_template('temperature.html', temp=temp_c, city= city, country=country)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

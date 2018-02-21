from flask import Flask, render_template, request
import weather
import graphs

app = Flask(__name__)


@app.route('/response', methods=['POST'])
def response():
    city = request.form['city']
    weather_dict = weather.weatherData(city)
    dates = weather_dict['dates']
    days = weather.days(dates)
    magical_length = len(days)
    graph = graphs.graphs(weather_dict, dates)
    return render_template('index.html', length = magical_length, days = days, dates = dates, weather_dict = weather_dict, graph = graph)

@app.route('/')
def index():
    weather_dict = weather.weatherData('auckland')
    dates = weather_dict['dates']
    days = weather.days(dates)
    magical_length = len(days)
    graph = graphs.graphs(weather_dict, dates)
    return render_template('index.html', length = magical_length, days = days, dates = dates, weather_dict = weather_dict, graph = graph)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)

import pygal
import weather
from pygal.style import LightenStyle, LightColorizedStyle

def graphs(weather_dict, dates):
    '''
    This function takes weather data and outputs graphs for temperature, humidity and wind speeds.
    input:
    weather_dict = weather dictionary with relevant data
    dates = a list of dates, each date is a key for the dictionary
    output:
    graph = a list of three graphs, one each for temperature, humidity and windspeed, for each day.
            e.g. [[temp, humid, wind], [temp, humid, wind], etc...]

    '''
    graph= []
    for date in dates:
        temp_style = LightenStyle('#46C5EA', base_style=LightColorizedStyle)
        temp_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=temp_style)
        temp_chart.title = 'Temperature in degrees celsius'
        temp_chart.x_labels = map(str, weather_dict[date]['times'])
        temp_chart.add('Temperature',  weather_dict[date]['temps'])
        temp_chart = temp_chart.render_data_uri()

        humid_style = LightenStyle('#6E9DF6', base_style=LightColorizedStyle)
        humid_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=humid_style)
        humid_chart.title = 'Humidity as %'
        humid_chart.x_labels = map(str, weather_dict[date]['times'])
        humid_chart.add('Humidity',  weather_dict[date]['humidity'])
        humid_chart = humid_chart.render_data_uri()

        wind_style = LightenStyle('#8A6DEC', base_style=LightColorizedStyle)
        wind_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=wind_style)
        wind_chart.title = 'Windspeed in m/s'
        wind_chart.x_labels = map(str, weather_dict[date]['times'])
        wind_chart.add('Wind speeds',  weather_dict[date]['windspeed'])
        wind_chart = wind_chart.render_data_uri()
        graph += [[temp_chart, humid_chart, wind_chart]]
    return graph

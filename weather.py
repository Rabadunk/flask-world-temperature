#Importing requests to request from url
import requests
import datetime
import calendar

def weatherData(city):
    '''
    This is a function that takes a city name and calls on the open weather api for
    weather data on the next 5 days for the city. It then organises relevant data needed for
    the app.
    input: city: city name
    output: days_dict: a dictionary in the form
    {date: list of times during the day in 3 hour intervals, list of temperatures for respective time,...
    ... list of humidities, average temperature for that day}
    there is also {dates: list of each date so that its easy to access keys}
    '''
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+city+'&appid=0cd5498b4fc08eb51125e83318e058ef')
    json_object = response.json()
    days_dict = {}
    dates = []
    for item in json_object['list']:
        if item['dt_txt'][:10] not in days_dict.keys():
            dates.append(item['dt_txt'][:10])
            days_dict[item['dt_txt'][:10]] = {'times': [item['dt_txt'][11:]], 'temps': [celsius(item['main']['temp'])], 'humidity': [str(item['main']['humidity']) + '%']}

        else:
            days_dict[item['dt_txt'][:10]]['times'].append(item['dt_txt'][11:])
            days_dict[item['dt_txt'][:10]]['temps'].append(celsius(item['main']['temp']))
            days_dict[item['dt_txt'][:10]]['humidity'].append(str(item['main']['humidity']) + '%')
    days_dict['dates'] = dates

    for day in dates:
        days_dict[day]['avg_temp'] = averageTemperature(days_dict[day]['temps'])

    return days_dict

def days(dates):
    '''
    This function takes a list of dates and returns a list with the corresponding
    days, i.e. 2018-02-18 is a wednesday.
    input: dates: list of dates
    output: days: list of days, eg. [monday, tuesday,...]
    '''
    days = []
    for date in dates:
        #formatting date
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])
        dateObject = datetime.date(year, month, day)
        day = calendar.day_name[dateObject.weekday()]
        days.append(day)
    return days

def celsius(tempk):
    '''
    this function takes a string variable tempk, a temperature in kelvin, and converts it
    to degrees celisius.
    input: tempk = temperature in kelvin (str)
    output: tempc = temperature in celsius (int)
    '''
    tempc = round(int(tempk) - 273.15)

    return tempc

def farenheit(tempk):
    '''
    this function takes a string variable tempk, a temperature in kelvin, and converts it
    to degrees farenheit.
    input: tempk = temperature in kelvin (str)
    output: tempf = temperature in farenheit (int)
    '''
    tempf = round(int(tempk) * 9/5 - 459.67)

    return tempf

def averageTemperature(temps):
    '''
    this function takes a list of temperatures and returns a single average value
    input: temps = list of temperatures
    output: avgTemp = average temperature (single integer)
    '''
    length = len(temps)
    total = 0

    for temp in temps:
        total += temp

    return round(total/length)

'''
for item in json_object['list']:
    #date
    print(item['dt_txt'][:10])
    #time
    print(item['dt_txt'][11:])
    #temp
    print(item['main']['temp'])
    #humidity
    print(str(item['main']['humidity']) + '%')
    #icon
    print(item['weather'][0]['main'])
    #description
    print(item['weather'][0]['description'])
    #main output
    print(item)
    print('######################################################################################' + str(COUNT))
    COUNT +=1
#print(json_object2['results'][0]['geometry']['location'])
'''

import requests

def get_data(url):
    response = requests.get(url)
    return response.json()['list']

def get_dates(data):
    dates = set()
    for date in data:
        dates.add(date['dt_txt'].split(' ')[0])
    return dates

def get_weather(data, date):
    avg_temperature = 0
    hours = 0
    print('\nHourly Temperature Forecast for '+date+'\n')
    for day in data:
        if day['dt_txt'].split(' ')[0] == date:
            avg_temperature += day['main']['temp']
            hours += 1
            print(day['dt_txt'].split(' ')[1],':',day['main']['temp'])
        
    print('\n=> Daily Average Temperature Forecast for '+date+" :",round(avg_temperature/hours, 2))

def get_wind_speed(data, date):
    avg_temperature = 0
    hours = 0
    print('\nHourly Wind Speed Forecast for '+date+'\n')
    for day in data:
        if day['dt_txt'].split(' ')[0] == date:
            avg_temperature += day['wind']['speed']
            hours += 1
            print(day['dt_txt'].split(' ')[1],':',day['wind']['speed'])
        
    print('\n=> Daily Average Wind Speed Forecast for '+date+" :",round(avg_temperature/hours, 2))

def get_pressure(data, date):
    avg_temperature = 0
    hours = 0
    print('\nHourly Temperature Forecast for '+date+'\n')
    for day in data:
        if day['dt_txt'].split(' ')[0] == date:
            avg_temperature += day['main']['pressure']
            hours += 1
            print(day['dt_txt'].split(' ')[1],':',day['main']['pressure'])
        
    print('\n=> Daily Average Pressure Forecast for '+date+" :",round(avg_temperature/hours, 2))
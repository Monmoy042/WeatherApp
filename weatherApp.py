## Weather App
#--------------
# DarkSky
from darksky import forecast
from datetime import date, timedelta

# OpenCage
from opencage.geocoder import OpenCageGeocode

# Coordinate find out
key = 'API Key' #Insert OpenCage API Key 
geocoder = OpenCageGeocode(key)
place = input('Enter a city name ')
location = geocoder.geocode(place)
# result = geocoder.geocode('London', no_annotations=1, language='es')
# result = geocoder.geocode('London', proximity='42.828576, -81.406643')
# print(result[0]['formatted'])
# print(result[0])

# Find out the latitude and longitude
latitude = (location[0]['geometry']['lat'])
longitude = (location[0]['geometry']['lng'])
print('Lat: ',latitude)
print('Lan: ',longitude)

# Find out the weather information from DarkSky API
Coordinate = latitude, longitude
weekday = date.today()
with forecast('API Key', *Coordinate) as coordinate: #Insert API key of DarkSky
    temp = (((coordinate.temperature)-32)/1.8)
    print('TimeZone: ',coordinate.timezone)
    print('Summary: ',coordinate.summary)
    print('Icon:',coordinate.icon)
    print('Temperature in Fahrenheit: ',coordinate.temperature)
    print('Temperature in degree celsius: ',"%.2f" %temp)
    print('Humidity: ',coordinate.humidity)
    print('WindSpeed: ',coordinate.windSpeed)
    print(coordinate.hourly.summary)


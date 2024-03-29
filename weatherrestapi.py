import requests
url = "https://www.metaweather.com/api/location/search/?query=bangalore"
response = requests.get(url)

[weather_response] = response.json()
woeid_value = weather_response["woeid"]

woeid_url = "https://www.metaweather.com/api/location/" + str(woeid_value) + "/"
woeid_response = requests.get(woeid_url).json()
weather_for_the_day = woeid_response["consolidated_weather"][0]["weather_state_name"]
print(weather_for_the_day)

import os
from datetime import datetime
user_id = "7ee42fbaaebd27021ed55a3bafd17498"
location = input("Enter the city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_id
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)
if api_data['cod'] == '404':
   print ("Invalid city: {}, Please check your city name".format(location))
else:
    temp_city = ((api_data['main']['temp'])-273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    print("weather states for - {} || {}".format(location.upper(),date_time))
    print("Current temp is: {:.2f} deg C".format(temp_city))
    print("Current humidity     :",hmdt)
    print("Current weather desc :",weather_desc)
    print("Current time         :",date_time)


import datetime
import requests



_url = 'http://api.openweathermap.org/data/2.5/weather?'
city = input()
if not city:
    pass
api_key = 'fe8d8c65cf345889139d8e545f57819a'
all_url = _url + 'appid=' + api_key + '&q=' + city + '&units=metric'
rp = requests.get(all_url)
data = rp.json()
if data['cod'] != '404':
    we_res = data['weather']
    city_res = data['main']
    nhiet = city_res['temp']
    apsuat = city_res['pressure']
    doam = city_res['humidity']
    trangthai = we_res[0]['description']
    mt = data['sys']
    mtmoc = datetime.datetime.fromtimestamp(mt['sunrise'])
    mtlan = datetime.datetime.fromtimestamp(mt['sunset'])
    wther = data['weather']
    weather_description = wther[0]['description']
    now = datetime.datetime.now()
    print("""\tmat troi moc {hourrise}:{minrise} ---- mat troi lan {hourset}:{minset}, 
nhiet do {temp} -- ap suat {pressure} -- do am {humidity} """.format(
        hourrise = mtmoc.hour, minrise = mtmoc.minute,
        hourset = mtlan.hour, minset = mtlan.minute,temp = nhiet, 
        pressure = apsuat, humidity = doam))
    print(trangthai)
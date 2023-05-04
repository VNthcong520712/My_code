import phonenumbers, opencage, folium
# from myphone import number

from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

pep = phonenumbers.parse("+919775567890")
local = geocoder.description_for_number(pep, "vi")
print(carrier.name_for_number(pep, 'vi'), local)
ser = carrier.name_for_number(pep, "vi")

key = "efa3975761ab4ab68cbbff8043cdc406"
geo = OpenCageGeocode(key)
que = str(local)
result = geo.geocode(que)
lat = result[0]["geometry"]["lat"]
lng = result[0]['geometry']['lng']
print(lat, lng)

map = folium.Map(location=[lat, lng], zoom_control=9)
folium.Marker([lat, lng], popup=local).add_to(map)
map.save("mylocation.html")
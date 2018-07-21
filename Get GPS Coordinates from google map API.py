
# coding: utf-8

import googlemaps
import pandas as pd

#open excel file, 
address = pd.read_excel('Trains_LatLong_Input.xlsx')

Address=address['StationName']

gmaps = googlemaps.Client(key='API KEY')

# Geocoding an address

lat,long=[],[]

for address in Address:
    try:
        geocode_result = gmaps.geocode(address)
        x=geocode_result[0]['geometry']['location']['lat']
        y=geocode_result[0]['geometry']['location']['lng']
        print(x,y)
        lat.append(x)
        long.append(y)
    except Exception as e:
        print('Error, skipping address...', e, ' ', address)




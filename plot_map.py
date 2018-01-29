# --- Code for creating scatter maps:
# Credits: Manoj Pravakar Saha on https://manojsaha.com/2017/03/08/drawing-locations-google-maps-python/

# --- Code for converting longitude and latitude values to cities:
# https://stackoverflow.com/questions/20169467/how-to-convert-from-longitude-and-latitude-to-country-or-city

import gmplot

#Set the cursor
# cur = db_conn.cursor()

# Initialize two empty lists to hold the latitude and longitude values
latitude = [40.647675, 49.856922]
longitude = [-73.983834, 9.985637]

# TODO: Convert column "geo_location" to longitude and latitude, and scatter randomly for better visualization 

# Geolocate all geo_locations via a query to an address and coordinates:
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Barcelona")
print(location.address)
print((location.latitude, location.longitude))
# Add all found coordinates to corresponding lists:
latitude.append(location.latitude)
longitude.append(location.longitude)

# Initialize the map to the first location in the list
gmap = gmplot.GoogleMapPlotter(latitude[0],longitude[0], 4)

# Draw the points on the map. I created my own marker for '#FF66666'. 
# You can use other markers from the available list of markers. 
# Another option is to place your own marker in the folder - 
# /usr/local/lib/python3.5/dist-packages/gmplot/markers/
gmap.scatter(latitude, longitude, '#FF6666', size=40000, marker=False)

# Write the map in an HTML file
gmap.draw('map.html')

# Close the cursor and the database connection 
# cur.close()
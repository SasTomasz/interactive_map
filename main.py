import folium
import pandas

# location where map starts
MY_LOCATION = (50.061695, 19.936030)
ZOOM = 15
MAP_SOURCE = "Stamen Terrain"

# create base maps with Stamen Terrain service
my_map = folium.Map(MY_LOCATION, zoom_start=ZOOM, tiles=MAP_SOURCE)

# add first layer
layer_1 = folium.FeatureGroup("pointer")
marker = folium.Marker(MY_LOCATION, "We start here")
layer_1.add_child(marker)

# add multiple markers from file
locations_file = pandas.read_excel("Locations.xlsx")

for i in range(locations_file.index.size):
    longitude = locations_file.iloc[i, 0]   # first column in file with longitude
    latitude = locations_file.iloc[i, 1]    # second column in file with latitude
    location = (longitude, latitude)
    layer_1.add_child(folium.Marker(location))

# add layers to map
my_map.add_child(layer_1)

# save map
my_map.save("my_map.html")
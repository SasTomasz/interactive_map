import folium
import pandas

# location where map starts
MY_LOCATION = (50.061695, 19.936030)
ZOOM = 15
MAP_SOURCE = "Stamen Terrain"

locations_file = pandas.read_excel("Locations.xlsx")
lon = list(locations_file["Longitude"])
lat = list(locations_file["Latitude"])

# create base maps with Stamen Terrain service
my_map = folium.Map(MY_LOCATION, zoom_start=ZOOM, tiles=MAP_SOURCE)

# add first layer
layer_1 = folium.FeatureGroup("pointer")
marker = folium.Marker(MY_LOCATION, "We start here")
layer_1.add_child(marker)

# add multiple markers from file
for ln, lt in zip(lon, lat):
    layer_1.add_child(folium.Marker((ln, lt)))

# add layers to map
my_map.add_child(layer_1)

# save map
my_map.save("my_map.html")
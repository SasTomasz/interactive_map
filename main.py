import folium
import pandas

# location where map starts
MY_LOCATION = (50.061695, 19.936030)
ZOOM = 15
MAP_SOURCE = "Stamen Terrain"

volcanoes_file = pandas.read_csv("Volcanoes.txt")
volcanoes_lat = list(volcanoes_file["LAT"])
volcanoes_lon = list(volcanoes_file["LON"])
volcanoes_name = list(volcanoes_file["NAME"])


def add_markers(lat, lon, name):
    for lt, ln, nm in zip(lat, lon, name):
        layer_1.add_child(folium.Marker((lt, ln), popup=nm))

# create base maps with Stamen Terrain service
my_map = folium.Map(MY_LOCATION, zoom_start=ZOOM, tiles=MAP_SOURCE)

# add first layer
layer_1 = folium.FeatureGroup("pointer")
marker = folium.Marker(MY_LOCATION, "We start here")
layer_1.add_child(marker)

add_markers(volcanoes_lat, volcanoes_lon, volcanoes_name)

# add layers to map
my_map.add_child(layer_1)

# save map
my_map.save("my_map.html")
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
volcanoes_elev = list(volcanoes_file["ELEV"])

html = """Volcano name:<br>
<a href="http://www.google.com/search?q=%%22%s%%22" target="blank">%s</a><br>
Height: %s m"""

def color_marker(elev):
    match elev: 
        case elev if elev < 1500:
            return "green"

        case elev if 1500 <= elev < 3000:
            return "orange"

        case elev if elev >= 3000:
            return "red"

        case _:
            return "black"


def add_markers(lat, lon, name, elev):
    for lt, ln, nm, el in zip(lat, lon, name, elev):
        iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
        layer_1.add_child(folium.CircleMarker((lt, ln), radius=6, popup=folium.Popup(iframe), color="gray", 
            fill_color = color_marker(el), fill_opacity = 0.7))

# create base maps with Stamen Terrain service
my_map = folium.Map(MY_LOCATION, zoom_start=ZOOM, tiles=MAP_SOURCE)

# add first layer
layer_1 = folium.FeatureGroup("pointer")
marker = folium.Marker(MY_LOCATION, "We start here")
layer_1.add_child(marker)

add_markers(volcanoes_lat, volcanoes_lon, volcanoes_name, volcanoes_elev)

with open('world.json', 'r', encoding='utf-8-sig') as file: 
    json = file.read()

# add second layer
layer_2 = folium.FeatureGroup("country")
layer_2.add_child(folium.GeoJson(data=json, 
style_function = lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red'}))

# add layers to map
my_map.add_child(layer_2)
my_map.add_child(layer_1)

# save map
my_map.save("my_map.html")
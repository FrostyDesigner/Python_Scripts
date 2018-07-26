#first import the library
import folium

import pandas
data = pandas.read_csv("C:\GitHub\Python_Scripts\WebmapsWithFolium\Volcanoes.csv")
#data.columns   -   to return all columns
#then create list from columns - "Longitude" is a column name
lon = list(data["Longitude"])
lat = list(data["Latitude"])
elev = list(data["Elev"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


#create map object
map = folium.Map(location=[40.59, -75.50], zoom_start=5)

#add marker to map
fgv = folium.FeatureGroup(name="Volcanoes")
#between map and save method can add objects to map

#change the color dynamically
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m", 
    fill_color=color_producer(el), color = 'grey', fill=True , fill_opacity=0.7))

#add marker to map
fgp = folium.FeatureGroup(name="Population")

#add geojson data layer to map
fgp.add_child(folium.GeoJson(data=open("C:\GitHub\Python_Scripts\WebmapsWithFolium\world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())


map.save("C:\GitHub\Python_Scripts\WebmapsWithFolium\World_Map.html")

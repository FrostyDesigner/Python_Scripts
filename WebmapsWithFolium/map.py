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
map = folium.Map(location=[40.59, -75.50])
#save it somewhere as html
map.save("C:\GitHub\Python_Scripts\WebmapsWithFolium\Map.html")

#with zoom parameter
map = folium.Map(location=[40.59, -75.50], zoom_start=6)
#you can save as another html or save it as the same html and just refresh the browser
map.save("C:\GitHub\Python_Scripts\WebmapsWithFolium\Map_zoom.html")

#on a different layer
map = folium.Map(location=[40.59, -75.50], zoom_start=6, tiles="Mapbox Bright")
map.save("C:\GitHub\Python_Scripts\WebmapsWithFolium\Map_tiles.html")
map = folium.Map(location=[40.59, -75.50], zoom_start=6, tiles="Mapbox Bright")

#add marker to map
fg = folium.FeatureGroup(name="My Map")
#between map and save method can add objects to map
fg.add_child(folium.Marker(location=[40.59, -75.50], popup="Allentown", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("C:\GitHub\Python_Scripts\WebmapsWithFolium\Map_tiles_marker.html")

#add multiple markers to map
fg2 = folium.FeatureGroup(name="My Map 2")
#deprecated
#for coordinates in [[40.59, -75.50], [39.59, -73.50]]:
#when iterating through more than one list you must use the zip() function
for lt, ln, el in zip(lat, lon, elev):
    #have to convert 'el' to striing because 'popup' wants a string
    #fg2.add_child(folium.Marker(location=[lt, ln], popup=str(el), icon=folium.Icon(color='green')))
    #need to parse string in case data has quotations that html cant interpret
    fg2.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el), parse_html=True), icon=folium.Icon(color='green')))
map.add_child(fg2)
map.save("C:\GitHub\Python_Scripts\WebmapsWithFolium\Map_tiles_multi_marker.html")

#add multiple markers to map
fg3 = folium.FeatureGroup(name="My Map 3")
#cahange the color dynamically
for lt, ln, el in zip(lat, lon, elev):
    #have to convert 'el' to striing because 'popup' wants a string
    #fg3.add_child(folium.Marker(location=[lt, ln], popup=str(el), icon=folium.Icon(color='green')))
    #need to parse string in case data has quotations that html cant interpret
    #favorite
    #fg3.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el), parse_html=True), icon=folium.Icon(color=color_producer(el))))
    #circle markers with opacity
    fg3.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m", 
    fill_color=color_producer(el), color = 'grey', fill=True , fill_opacity=0.7))

#add geojson data layer to map
#only needed to draw polygons around countries in this case
fg3.add_child(folium.GeoJson(data=(open("C:\GitHub\Python_Scripts\WebmapsWithFolium\world.json", 'r', encoding='utf-8-sig').read())))

map.add_child(fg3)
map.save("C:\GitHub\Python_Scripts\WebmapsWithFolium\Map_tiles_multicolor_marker.html")

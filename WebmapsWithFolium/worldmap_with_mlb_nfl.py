#first import the library
import folium
import pandas

#create map object
#between map and the final map.save method you can add objects to map
map = folium.Map(location=[40.59, -75.50], zoom_start=5)

#add population layer to map
fgp = folium.FeatureGroup(name="Population")

#add geojson data to map that will draw the map boundaries and populate them with color
fgp.add_child(folium.GeoJson(data=open("C:\GitHub\Python_Scripts\WebmapsWithFolium\world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red'}))

#add the volcano filter to map
fgv = folium.FeatureGroup(name="Volcanoes")

data = pandas.read_csv("C:\GitHub\Python_Scripts\WebmapsWithFolium\Volcanoes.csv")
#data.columns   -   to return all columns
#then create list from columns - "Longitude" is a column name
lon = list(data["Longitude"])
lat = list(data["Latitude"])
elev = list(data["Elev"])

#color volcanoes based on elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#change the color dynamically
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m", 
    fill_color=color_producer(el), color = 'grey', fill=True , fill_opacity=0.7))

#add filter to map
fgmlb = folium.FeatureGroup(name="MLB Stadiums")

#add mlb data to locate stadiums across the map
data_mlb = pandas.read_json("C:\GitHub\Python_Scripts\WebmapsWithFolium\mlb_stadiums.json")
lon_mlb = list(data_mlb["lng"])
lat_mlb = list(data_mlb["lat"])
team_mlb = list(data_mlb["team"])

#change the mlb icon color to red
for lt, ln, tm in zip(lat_mlb, lon_mlb, team_mlb):
    fgmlb.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(tm), parse_html=True), icon=folium.Icon(color="red")))

#add filter to map
fgnfl = folium.FeatureGroup(name="NFL Stadiums")

#add nfl data to locate stadiums across the map
data_nfl = pandas.read_csv("C:\\GitHub\\Python_Scripts\\WebmapsWithFolium\\nfl_stadiums.csv")
lon_nfl = list(data_nfl["longitude"])
lat_nfl = list(data_nfl["latitude"])
team_nfl = list(data_nfl["Team"])

#change the nfl icon color to blue
for lt, ln, tm in zip(lat_nfl, lon_nfl, team_nfl):
    fgnfl.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(tm), parse_html=True), icon=folium.Icon(color="blue")))

#construct the map
map.add_child(fgv)
map.add_child(fgp)
map.add_child(fgmlb)
map.add_child(fgnfl)
map.add_child(folium.LayerControl())

map.save("C:\GitHub\Python_Scripts\WebmapsWithFolium\World_Map_with_MLB_NFL.html")

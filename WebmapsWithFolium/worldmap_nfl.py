#first import the library
import folium
import pandas

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


#create map object
map = folium.Map(location=[40.59, -75.50], zoom_start=5)
#add group of markers to featureGroup
fgnfl = folium.FeatureGroup(name="NFL Stadiums")

#between map and save method can add objects to map
#add nfl data
#data = pandas.read_csv("C:\GitHub\Python_Scripts\WebmapsWithFolium\Volcanoes.csv")
data_nfl = pandas.read_csv("C:\\GitHub\\Python_Scripts\\WebmapsWithFolium\\nfl_stadiums.csv")
lon_nfl = list(data_nfl["longitude"])
lat_nfl = list(data_nfl["latitude"])
team_nfl = list(data_nfl["Team"])

#change the nfl icon color to blue
for lt, ln, tm in zip(lat_nfl, lon_nfl, team_nfl):
    fgnfl.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(tm), parse_html=True), icon=folium.Icon(color="blue")))

map.add_child(fgnfl)
map.add_child(folium.LayerControl())
map.save("C:\GitHub\Python_Scripts\WebmapsWithFolium\World_Map_NFL.html")
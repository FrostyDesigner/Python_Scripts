#first import the libraries
import folium
import pandas

data = pandas.read_csv("C:\GitHub\Python_Scripts\WebmapsWithFolium\Crimes_2015_Reduced.csv")
#data.columns   -   to return all columns
#then create list from columns - "Longitude" is a column name
lon = list(data["Longitude"])
lat = list(data["Latitude"])
ptype = list(data["Primary Type"])
desc = list(data["Description"])

def color_producer(primary_type):
    if primary_type == 'BURGLARY':
        return 'green'
    elif primary_type == 'OFFENSE INVOLVING CHILDREN':
        return 'orange'
    elif primary_type == 'BATTERY':
        return 'yellow'
    else:
        return 'red'

#create map object over city
map = folium.Map(location=[41.00, -87.00], zoom_start=8)

#between map and save method you can add objects to map
# BURGLARY
# OFFENSE INVOLVING CHILDREN
# BATTERY
# THEFT
# CRIMINAL DAMAGE
# ASSAULT
# DECEPTIVE PRACTICE
# OTHER OFFENSE
# CRIM SEXUAL ASSAULT
# PUBLIC PEACE VIOLATION
# NARCOTICS
# CRIMINAL TRESPASS


# BURGLARY
# OFFENSE INVOLVING CHILDREN
# BATTERY
# THEFT
# CRIMINAL DAMAGE
# ASSAULT
# DECEPTIVE PRACTICE
# OTHER OFFENSE
# CRIM SEXUAL ASSAULT
# PUBLIC PEACE VIOLATION
# NARCOTICS
# CRIMINAL TRESPASS
# MOTOR VEHICLE THEFT
# ROBBERY
# INTERFERENCE WITH PUBLIC OFFICER
# STALKING
# WEAPONS VIOLATION
# LIQUOR LAW VIOLATION
# SEX OFFENSE
#copy block to create new feature groups for the layer control object
#-----------------------------------------------------------------
#add marker to features group
fgb = folium.FeatureGroup(name="BURGLARY")
dfburglz = data.loc[data['Primary Type']=="BURGLARY"]

lon = list(data["Longitude"])
lat = list(data["Latitude"])
ptype = list(data["Primary Type"])
desc = list(data["Description"])

#change the color dynamically and add a popup
for lt, ln, prtype in zip(lat, lon, ptype):
    fgb.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(prtype)+" m", 
    fill_color=color_producer(prtype), color = 'grey', fill=True , fill_opacity=0.7))

#burglary filter
fg_b = folium.FeatureGroup(name="BURGLARY")
dfburglz = data.loc[data['Primary Type']=="BURGLARY"]
lon = list(dfburglz["Longitude"])
lat = list(dfburglz["Latitude"])
ptype = list(dfburglz["Primary Type"])
desc = list(dfburglz["Description"])
for lt, ln, prtype in zip(lat, lon, ptype):
    fg_b.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(prtype)+" m", 
    fill_color='red', color = 'grey', fill=True , fill_opacity=0.7))
map.add_child(fg_b)
#----------------------------
#OFFENSE INVOLVING CHILDREN filter
fg_oac = folium.FeatureGroup(name="OFFENSE INVOLVING CHILDREN")
df_oac = data.loc[data['Primary Type']=="OFFENSE INVOLVING CHILDREN"]
lon = list(df_oac["Longitude"])
lat = list(df_oac["Latitude"])
ptype = list(df_oac["Primary Type"])
desc = list(df_oac["Description"])
for lt, ln, prtype in zip(lat, lon, ptype):
    fg_oac.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(prtype)+" m", 
    fill_color='red', color = 'grey', fill=True , fill_opacity=0.7))
map.add_child(fg_oac)
#-------------------------------
#ALL Others filter
fg_all_others = folium.FeatureGroup(name="All OTHERS")
df_all_others = data.loc[data['Primary Type']!="BURGLARY"]
lon = list(df_all_others["Longitude"])
lat = list(df_all_others["Latitude"])
ptype = list(df_all_others["Primary Type"])
desc = list(df_all_others["Description"])
for lt, ln, prtype in zip(lat, lon, ptype):
    fg_all_others.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(prtype)+" m", 
    fill_color='red', color = 'grey', fill=True , fill_opacity=0.7))
map.add_child(fg_all_others)
#-------------------------------
#THEFT filter
fg_THEFT = folium.FeatureGroup(name="THEFT")
df_THEFT = data.loc[data['Primary Type']=="THEFT"]
lon = list(df_THEFT["Longitude"])
lat = list(df_THEFT["Latitude"])
ptype = list(df_THEFT["Primary Type"])
desc = list(df_THEFT["Description"])
for lt, ln, prtype in zip(lat, lon, ptype):
    fg_THEFT.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(prtype)+" m", 
    fill_color='red', color = 'grey', fill=True , fill_opacity=0.7))
map.add_child(fg_THEFT)
#-------------------------------
#CRIMINAL DAMAGE filter
fg_CRIMINAL_DAMAGE = folium.FeatureGroup(name="CRIMINAL DAMAGE")
df_CRIMINAL_DAMAGE = data.loc[data['Primary Type']=="CRIMINAL DAMAGE"]
lon = list(df_CRIMINAL_DAMAGE["Longitude"])
lat = list(df_CRIMINAL_DAMAGE["Latitude"])
ptype = list(df_CRIMINAL_DAMAGE["Primary Type"])
desc = list(df_CRIMINAL_DAMAGE["Description"])
for lt, ln, prtype in zip(lat, lon, ptype):
    fg_CRIMINAL_DAMAGE.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(prtype)+" m", 
    fill_color='red', color = 'grey', fill=True , fill_opacity=0.7))    
map.add_child(fg_CRIMINAL_DAMAGE)
#-------------------------------
#ASSAULT filter
fg_ASSAULT = folium.FeatureGroup(name="ASSAULT")
df_ASSAULT = data.loc[data['Primary Type']=="ASSAULT"]
lon = list(df_ASSAULT["Longitude"])
lat = list(df_ASSAULT["Latitude"])
ptype = list(df_ASSAULT["Primary Type"])
desc = list(df_ASSAULT["Description"])
for lt, ln, prtype in zip(lat, lon, ptype):
    fg_ASSAULT.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(prtype)+" m", 
    fill_color='red', color = 'grey', fill=True , fill_opacity=0.7))    
map.add_child(fg_ASSAULT)
#-------------------------------
#DECEPTIVE PRACTICE filter
fg_DECEPTIVE_PRACTICE = folium.FeatureGroup(name="DECEPTIVE PRACTICE")
df_DECEPTIVE_PRACTICE = data.loc[data['Primary Type']=="DECEPTIVE PRACTICE"]
lon = list(df_DECEPTIVE_PRACTICE["Longitude"])
lat = list(df_DECEPTIVE_PRACTICE["Latitude"])
ptype = list(df_DECEPTIVE_PRACTICE["Primary Type"])
desc = list(df_DECEPTIVE_PRACTICE["Description"])
# for lt, ln, prtype in zip(lat, lon, ptype):
#     fg_DECEPTIVE_PRACTICE.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(prtype)+" m", 
#     fill_color='red', color = 'grey', fill=True , fill_opacity=0.7))  
for lt, ln, prtype in zip(lat, lon, ptype):
    fg_DECEPTIVE_PRACTICE.add_child(folium.)    
map.add_child(fg_DECEPTIVE_PRACTICE)
#-------------------------------

#add a layer control object
map.add_child(folium.LayerControl())

#create map
map.save("C:\GitHub\Python_Scripts\WebmapsWithFolium\Chicago_Crimes_Reduced.html")

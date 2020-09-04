import folium
import os
import pandas as pd

m = folium.Map(location=[43.6819, -70.4490],
               tiles='OpenStreetMap',
               zoom_start=17,
               prefer_canvas=True
               )

residentiallots = "/home/root1/PycharmProjects/CampusParkingMap/GeoJSON/Residential Lots/"
commuterlots = "/home/root1/PycharmProjects/CampusParkingMap/GeoJSON/Commuter Lots/"
stafflots = "/home/root1/PycharmProjects/CampusParkingMap/GeoJSON/Staff Lots/"

commuterstyle = {'fillColor': 'red', 'color': 'black', 'fillOpacity': '0.4'}
residentialstyle = {'fillColor': 'green', 'color': 'black', 'fillOpacity': '0.4'}
staffstyle = {'fillColor': 'blue', 'color': 'black', 'fillOpacity': '0.4'}
closedlots = {'fillColor': 'black', 'color': 'black', 'fillOpacity': '0.4'}

colnames = ['lot_id', 'lot_name', 'lot_type', 'lot_status']
data = pd.read_csv('lots_mastersheet.csv', names=colnames)

# Residential Lots
resdirectory = os.fsencode(residentiallots)

for file in os.listdir(resdirectory):
    filename = os.fsdecode(file)
    if filename.endswith(".geojson"):
        folium.GeoJson(
            residentiallots + filename,
            style_function=lambda x: residentialstyle,
        ).add_to(m)
        continue

# Commuter Lots
commdirectory = os.fsencode(commuterlots)

for file in os.listdir(commdirectory):
    filename = os.fsdecode(file)
    if filename.endswith(".geojson"):
        folium.GeoJson(
            commuterlots + filename,
            style_function=lambda x: commuterstyle,
        ).add_to(m)
        continue

# Staff Lots
staffdirectory = os.fsencode(stafflots)

for file in os.listdir(staffdirectory):
    filename = os.fsdecode(file)
    if filename.endswith(".geojson"):
        folium.GeoJson(
            stafflots + filename,
            style_function=lambda x: staffstyle,
            name='G7',
        ).add_to(m)
        continue

m.save('/home/root1/PycharmProjects/CampusParkingMap/HTML Files/GorhamMap.html')   # allows for viewing of the map

#!/usr/bin/env python
# coding: utf-8

# In[1]:


def getmap():
    import folium
    import os
    import pandas as pd

    m = folium.Map(location=[43.6819, -70.4490],
               tiles='OpenStreetMap',
               zoom_start=17,
               prefer_canvas=True
               )

    residentiallots = r"/home/carter/Desktop/webmap_app/Resources/GeoJSON/Residential Lots/"
    commuterlots = r"/home/carter/Desktop/webmap_app/Resources/GeoJSON/Commuter Lots"
    stafflots = r"/home/carter/Desktop/webmap_app/Resources/GeoJSON/Staff Lots"

    commuterstyle = {'fillColor': 'red', 'color': 'black', 'fillOpacity': '0.4'}
    residentialstyle = {'fillColor': 'green', 'color': 'black', 'fillOpacity': '0.4'}
    staffstyle = {'fillColor': 'blue', 'color': 'black', 'fillOpacity': '0.4'}
    closedlots = {'fillColor': 'black', 'color': 'black', 'fillOpacity': '0.4'}

    colnames = ['lot_id', 'lot_name', 'lot_type', 'lot_status']
    data = pd.read_csv(r"/home/carter/Desktop/webmap_app/Resources/lots_mastersheet.csv", names=colnames)

    # Residential Lots
    resdirectory = os.fsencode(residentiallots)

    for file in os.listdir(resdirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".geojson"):
            folium.GeoJson(
            os.path.join(residentiallots, filename),
            style_function=lambda x: residentialstyle,
            highlight_function=lambda x: {'weight':3, 'color':'red','fillColor':'grey'},
            tooltip=folium.Tooltip('Residential lot, Click for more information!'),
            ).add_child(folium.Popup('Name:-\nAvailability Status:-')).add_to(m)
            continue

    # Commuter Lots
    commdirectory = os.fsencode(commuterlots)

    for file in os.listdir(commdirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".geojson"):
            folium.GeoJson(
               os.path.join(commuterlots, filename),
               style_function=lambda x: commuterstyle,
               highlight_function=lambda x: {'weight':3, 'color':'red','fillColor':'grey'},
               tooltip=folium.Tooltip('Commuter lot, Click for more information!'),
               ).add_child(folium.Popup('Name:-\nAvailability Status:-')).add_to(m)
            continue

    # Staff Lots
    staffdirectory = os.fsencode(stafflots)

    for file in os.listdir(staffdirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".geojson"):
            folium.GeoJson(
            os.path.join(stafflots, filename),
            style_function=lambda x: staffstyle,
            highlight_function=lambda x: {'weight':3, 'color':'red','fillColor':'grey'},
            tooltip=folium.Tooltip('Staff lot, Click for more information!'),
            name='G7',
            ).add_child(folium.Popup('Name:G7\nAvailability Status:-')).add_to(m)
            continue

    m.save(r"/home/carter/Desktop/webmap_app/templates/GorhamMap.html") 


# In[ ]:





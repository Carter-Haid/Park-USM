#!/usr/bin/env python
# coding: utf-8

# In[1]:


def getmap():
    import folium
    import os
    import json

    m = folium.Map(location=[43.6819, -70.4490],
                   tiles='OpenStreetMap',
                   zoom_start=17,
                   prefer_canvas=True
                   )

    residentiallots = r"/home/carter/PycharmProjects/campusParkingMap/Resources/GeoJSON/Residential Lots"
    commuterlots = r"/home/carter/PycharmProjects/campusParkingMap/Resources/GeoJSON/Commuter Lots"
    stafflots = r"/home/carter/PycharmProjects/campusParkingMap/Resources/GeoJSON/Staff Lots"

    commuterstyle = {'fillColor': 'red', 'color': 'black', 'fillOpacity': '0.4'}
    residentialstyle = {'fillColor': 'green', 'color': 'black', 'fillOpacity': '0.4'}
    staffstyle = {'fillColor': 'blue', 'color': 'black', 'fillOpacity': '0.4'}
    closedlots = {'fillColor': 'black', 'color': 'black', 'fillOpacity': '0.4'}

    # Residential Lots
    resdirectory = os.fsencode(residentiallots)

    for file in os.listdir(resdirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".json5"):
            folium.GeoJson(
                os.path.join(residentiallots, filename),
                style_function=lambda x: residentialstyle,
                highlight_function=lambda x: {'weight': 3, 'color': 'green', 'fillColor': 'grey'},
                popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                          aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'], class_name="respopup")
            ).add_to(m)
            continue

    # Commuter Lots
    commdirectory = os.fsencode(commuterlots)

    for file in os.listdir(commdirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".json5"):
            folium.GeoJson(
                os.path.join(commuterlots, filename),
                style_function=lambda x: commuterstyle,
                highlight_function=lambda x: {'weight': 3, 'color': 'red', 'fillColor': 'grey'},
                popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                          aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'], class_name="commpopup")
            ).add_to(m)
            continue

    # Staff Lots
    staffdirectory = os.fsencode(stafflots)

    for file in os.listdir(staffdirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".json5"):
            folium.GeoJson(
                os.path.join(stafflots, filename),
                style_function=lambda x: staffstyle,
                highlight_function=lambda x: {'weight': 3, 'color': 'blue', 'fillColor': 'grey'},
                popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                          aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'], class_name="staffpopup")
            ).add_to(m)
        continue

    m.save(r"/home/carter/PycharmProjects/campusParkingMap/templates/GorhamMap.html")

# In[ ]:


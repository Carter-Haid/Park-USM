#!/usr/bin/env python
# coding: utf-8

# In[1]:

def getmaptest():
    import folium
    import os
    import json

    m = folium.Map(location=[43.6819, -70.4490],
                   tiles='OpenStreetMap',
                   zoom_start=17,
                   prefer_canvas=True
                   )

    commuterstyle = {'fillColor': 'red', 'color': 'black', 'fillOpacity': '0.4'}
    residentialstyle = {'fillColor': 'green', 'color': 'black', 'fillOpacity': '0.4'}
    staffstyle = {'fillColor': 'blue', 'color': 'black', 'fillOpacity': '0.4'}
    closedstyle = {'fillColor': 'black', 'color': 'black', 'fillOpacity': '0.4'}

    path = r"/tests"

    for file in os.listdir(path):
        with open(os.path.join(path, file), "r+") as jsonFile:
            print(os.path.join(path, file))
            data = json.load(jsonFile)
            if data["features"][0]["properties"]["lot_status"] == "closed":
                folium.GeoJson(file, style_function=lambda x: closedstyle,
                               highlight_function=lambda x: {'weight': 3, 'color': 'black', 'fillColor': 'grey'},
                               popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                                         aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'],
                                                         class_name="closedpopup")
                               ).add_to(m)
            else:
                if data["features"][0]["properties"]["lot_type"] == "residential":
                    folium.GeoJson(file, style_function=lambda x: residentialstyle,
                                   highlight_function=lambda x: {'weight': 3, 'color': 'green', 'fillColor': 'grey'},
                                   popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                                             aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'],
                                                             class_name="respopup")
                                   ).add_to(m)
                if data["features"][0]["properties"]["lot_type"] == "commuter":
                    folium.GeoJson(file, style_function=lambda x: commuterstyle,
                                   highlight_function=lambda x: {'weight': 3, 'color': 'red', 'fillColor': 'grey'},
                                   popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                                             aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'],
                                                             class_name="commpopup")
                                   ).add_to(m)
                if data["features"][0]["properties"]["lot_type"] == "staff":
                    folium.GeoJson(file, style_function=lambda x: staffstyle,
                                   highlight_function=lambda x: {'weight': 3, 'color': 'blue', 'fillColor': 'grey'},
                                   popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                                             aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'],
                                                             class_name="staffpopup")
                                   ).add_to(m)

    m.save(r"/home/carter/PycharmProjects/campusParkingMap/templates/TestMap.html")

# In[ ]:

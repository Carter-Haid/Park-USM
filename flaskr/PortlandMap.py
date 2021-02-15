#!/usr/bin/env python
# coding: utf-8

# In[1]:

def portlandmap():
    import folium
    import os
    import json

    m = folium.Map(location=[43.6622, -70.2755],
                   tiles='OpenStreetMap',
                   prefer_canvas=True,
                   zoom_control=False
                   )

    residentiallots = "/home/carter/PycharmProjects/campusParkingMap/flaskr/Resources/GeoJSON/Portland/Residential Lots"
    commuterlots = "/home/carter/PycharmProjects/campusParkingMap/flaskr/Resources/GeoJSON/Portland/Commuter Lots"
    stafflots = "/home/carter/PycharmProjects/campusParkingMap/flaskr/Resources/GeoJSON/Portland/Staff Lots"

    commuterstyle = {'fillColor': 'red', 'color': 'black', 'fillOpacity': '0.5'}
    residentialstyle = {'fillColor': 'green', 'color': 'black', 'fillOpacity': '0.6'}
    staffstyle = {'fillColor': 'blue', 'color': 'black', 'fillOpacity': '0.6'}
    closedstyle = {'fillColor': 'black', 'color': 'black', 'fillOpacity': '0.6'}

    portlandbancounter = 0

    # Residential Lots
    resdirectory = os.fsencode(residentiallots)

    for file in os.listdir(resdirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".json5"):
            with open(residentiallots + "/" + filename) as f:
                data = json.load(f)
                if data['features'][0]['properties']['lot_status'] == 'closed':
                    folium.GeoJson(
                        os.path.join(residentiallots, filename),
                        style_function=lambda x: closedstyle,
                        highlight_function=lambda x: {'weight': 3, 'color': 'black', 'fillColor': 'grey'},
                        popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                                  aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'],
                                                  class_name="respopup")
                    ).add_to(m)
                    portlandbancounter += 1
                else:
                    folium.GeoJson(
                        os.path.join(residentiallots, filename),
                        style_function=lambda x: residentialstyle,
                        highlight_function=lambda x: {'weight': 3, 'color': 'green', 'fillColor': 'grey'},
                        popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                                  aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'],
                                                  class_name="respopup")
                    ).add_to(m)
            continue

    # Commuter Lots
    commdirectory = os.fsencode(commuterlots)

    for file in os.listdir(commdirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".json5"):
            with open(commuterlots + "/" + filename) as f:
                data = json.load(f)
                if data['features'][0]['properties']['lot_status'] == 'closed':
                    folium.GeoJson(
                        os.path.join(commuterlots, filename),
                        style_function=lambda x: closedstyle,
                        highlight_function=lambda x: {'weight': 3, 'color': 'black', 'fillColor': 'grey'},
                        popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                                  aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'],
                                                  class_name="commpopup")
                    ).add_to(m)
                    portlandbancounter += 1
                else:
                    folium.GeoJson(
                        os.path.join(commuterlots, filename),
                        style_function=lambda x: commuterstyle,
                        highlight_function=lambda x: {'weight': 3, 'color': 'red', 'fillColor': 'grey'},
                        popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                                  aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'],
                                                  class_name="commpopup")
                    ).add_to(m)
            continue

    # Staff Lots
    staffdirectory = os.fsencode(stafflots)

    for file in os.listdir(staffdirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".json5"):
            with open(stafflots + "/" + filename) as f:
                data = json.load(f)
                if data['features'][0]['properties']['lot_status'] == 'closed':
                    folium.GeoJson(
                        os.path.join(stafflots, filename),
                        style_function=lambda x: closedstyle,
                        highlight_function=lambda x: {'weight': 3, 'color': 'black', 'fillColor': 'grey'},
                        popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                                  aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'],
                                                  class_name="staffpopup")
                    ).add_to(m)
                    portlandbancounter += 1
                else:
                    folium.GeoJson(
                        os.path.join(stafflots, filename),
                        style_function=lambda x: staffstyle,
                        highlight_function=lambda x: {'weight': 3, 'color': 'blue', 'fillColor': 'grey'},
                        popup=folium.GeoJsonPopup(fields=['lot_name', 'lot_type', 'lot_status'],
                                                  aliases=['Lot Name:', 'Lot Type:', 'Lot Status:'],
                                                  class_name="staffpopup")
                    ).add_to(m)
            continue

    m.fit_bounds([[43.6589, -70.2777], [43.6656, -70.27427]])
    m.save("/home/carter/PycharmProjects/campusParkingMap/flaskr/static/PortlandMap.html")
    return portlandbancounter

# In[ ]:

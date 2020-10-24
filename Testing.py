import json

# This opens a specefic JSON File and changes some data
with open("/home/carter/PycharmProjects/campusParkingMap/Resources/GeoJSON/Commuter Lots/G2a.json5", "r+") as jsonFile:
    data = json.load(jsonFile)

    data["features"][0]["properties"]["lot_status"] = "closed"
    data["features"][0]["properties"]["lot_name"] = "SOME OTHER LOT NAME"
    data["features"][0]["properties"]["lot_type"] = "residential"

    jsonFile.seek(0)
    json.dump(data, jsonFile)
    jsonFile.truncate()


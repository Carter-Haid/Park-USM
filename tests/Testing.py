import json

# NOTE THIS FILE DOES NOT RUN DO NOT RUN IT!

with open("/Resources/GeoJSON/Commuter Lots/G2a.json5", "r+") as jsonFile:
    data = json.load(jsonFile)

    data["features"][0]["properties"]["lot_status"] = "closed"
    #data["features"][0]["properties"]["lot_name"] = "SOME OTHER LOT NAME"
    #data["features"][0]["properties"]["lot_type"] = "residential"

    jsonFile.seek(0)
    json.dump(data, jsonFile)
    jsonFile.truncate()


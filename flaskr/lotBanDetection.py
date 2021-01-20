import os.path


# Gorham Lots
for dirpath, dirnames, filenames in os.walk("/home/carter/PycharmProjects/campusParkingMap/flaskr/Resources/GeoJSON/Gorham"):
    for filename in [f for f in filenames if f.endswith(".json5")]:
        print(os.path.join(dirpath, filename))


# Portland Lots
for dirpath, dirnames, filenames in os.walk("/home/carter/PycharmProjects/campusParkingMap/flaskr/Resources/GeoJSON/Portland"):
    for filename in [f for f in filenames if f.endswith(".json5")]:
        print(os.path.join(dirpath, filename))

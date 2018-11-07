import csv
import os

cities = {}
with open("cities.csv") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader, start=1):
        cities[row["Name"]] = i

dir = os.listdir("cities")
for name in dir:
    print(name)
    elements = []
    with open("cities/" + name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            elements.append((row["FIPS"], row["Lng"], row["Lat"], str(float(row["Duration"])), row["Density"]))

    with open("cities/" + name[name.index(" ")+1:], "w+") as file:
        file.write("FIPS,Lng,Lat,Duration,Density\n")
        for element in elements:
            file.write(element[0] + "," + element[1] + "," + element[2] + "," + element[3] + "," + element[4] + "\n")

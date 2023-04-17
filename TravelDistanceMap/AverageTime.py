import csv
import os

coords = {}
with open("TravelDistanceMap/convention_centers.csv", "r", encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        coords[row["Name"]] = (row["Lng"], row["Lat"])

cities = {}
for name in os.listdir("TravelDistanceMap/times"):
    with open("TravelDistanceMap/times/" + name) as file:
        reader = csv.DictReader(file)
        tmp = []
        for row in reader:
            tmp.append((float(row["Duration"]), float(row["Density"])))
        cities[name[:name.index(".")]] = tmp

with open("TravelDistanceMap/average_times.csv", "w+") as file:
    file.write("City,AvgDuration,Lng,Lat\n")
    for city in cities.items():
        average = sum([x[0]*x[1] for x in city[1]])/sum([x[1] for x in city[1]])
        print(city[0])
        file.write(city[0] + "," + str(average) + "," + coords[city[0]][0] + "," + coords[city[0]][1] + "\n")
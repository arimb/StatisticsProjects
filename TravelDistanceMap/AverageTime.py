import csv
import os

cities = {}
for name in os.listdir("cities"):
    with open("cities/" + name) as file:
        reader = csv.DictReader(file)
        tmp = []
        for row in reader:
            tmp.append((float(row["Duration"]), float(row["Density"])))
        cities[name[:name.index(".")]] = tmp

with open("averages.csv", "w+") as file:
    file.write("City,AvgDuration\n")
    for city in cities.items():
        average = sum([x[0]*x[1] for x in city[1]])/sum([x[1] for x in city[1]])
        print(city[0] + " - " + str(average))
        file.write(city[0] + "," + str(average) + "\n")
import csv
import os

def score(time):
    return (time + (3 if (time>1) else 0)) if (time<15) else (25 + (time-15)/4)

data = {}
for name in os.listdir("times/"):
    with open("times/" + name) as file:
        tmp = {}
        reader = csv.DictReader(file)
        for row in reader:
            tmp[row["FIPS"]] = (row["Lng"], row["Lat"], float(row["Duration"]), int(row["Density"]))
        data[name[:name.index(".")]] = tmp

averages = []
for city1 in data:
    for city2 in data:
        if city2 < city1: continue
        print(city1 + " " + city2)

        dim = sum([data[city1][c][3] for c in data[city1]])
        list1 = {}
        list2 = {}

        counties = []
        for county in data[city1]:
            counties.append((county, score(data[city1][county][2]) - score(data[city2][county][2])))
        counties = sorted(counties, key=lambda x:x[1])

        for county in counties:
            if sum([data[city1][c][3] for c in list1]) <= dim/2:
                list1[county[0]] = data[city1][county[0]]
            else:
                list2[county[0]] = data[city2][county[0]]

        averages.append((city1, city2,
                         (sum([list1[c][2]*score(list1[c][3]) for c in list1]) +
                          sum([list2[c][2]*score(list2[c][3]) for c in list2])) / dim))

with open("2champs_weighted.csv", "w+") as file:
    file.write("City1,City2,AvgScore\n")
    for pair in averages:
        file.write(pair[0] + "," + pair[1] + "," + str(pair[2]) + "\n")
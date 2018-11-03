import requests
import csv
from retrying import retry
import polyline

@retry(wait_fixed=5000)
def get_route(coords):
    ans = requests.get("http://router.project-osrm.org/route/v1/driving/" + coords + "?overview=full").json()
    if ans is None or ans == {'message': 'Too Many Requests'}:
        raise Exception("Too Many Requests")
    return ans

counties = {}
with open("team_counties.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["FIPS"] not in counties:
            counties[row["FIPS"]] = [0, (row["lng"], row["lat"])]
        counties[row["FIPS"]][0] += 1
num = len(counties)

cities = {}
with open("cities.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cities[row["Name"]] = (row["Lng"], row["Lat"])

for city in cities.items():
    print(city[0])
    steps = {}
    with open("cities/" + city[0] + ".csv", "w+") as file:
        file.write("FIPS,Lng,Lat,Duration,Density\n")
        for i, county in enumerate(counties.items(), start=1):
                route = get_route(city[1][0] + "," + city[1][1] + ";" + county[1][1][0] + "," + county[1][1][1])
                if route["code"] == "NoRoute":
                    continue
                try:
                    print(str(i) + "/" + str(num) + " " + county[0] + " (" + str(county[1][0]) + "): " + str(route["routes"][0]["duration"]))
                except:
                    print(county)
                    print(route)
                file.write(county[0] + "," + county[1][1][0] + "," + county[1][1][1] + "," + str(route["routes"][0]["duration"]) + "," + str(county[1][0]) + "\n")
                line = polyline.decode(route["routes"][0]["geometry"])
                for step in line:
                    if step not in steps:
                        steps[step] = 0
                    steps[step] += county[1][0]

    with open("paths/" + city[0] + ".csv", "w+") as pathfile:
        pathfile.write("Lat,Lng,Density\n")
        for step in steps.items():
            pathfile.write(str(step[0][0]) + "," + str(step[0][1]) + "," + str(step[1]) + "\n")

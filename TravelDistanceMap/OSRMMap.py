import requests
import csv
from retrying import retry
import polyline
import os

@retry(wait_fixed=5000)
def get_route(coords):
    ans = requests.get("http://router.project-osrm.org/route/v1/driving/" + coords + "?overview=full").json()
    if ans is None or ans == {'message': 'Too Many Requests'}:
        raise Exception("Too Many Requests")
    return ans

counties = {}
with open("TravelDistanceMap/team_counties.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["FIPS"] not in counties:
            counties[row["FIPS"]] = [0, (row["lng"], row["lat"])]
        counties[row["FIPS"]][0] += 1
num = len(counties)

cities = {}
with open("TravelDistanceMap/convention_centers.csv", "r", encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cities[row["Name"]] = (row["Lng"], row["Lat"])

done = os.listdir("TravelDistanceMap/cities")

for city, city_pos in cities.items():
    if (city+".csv") in done: continue
    print(city)
    steps = {}
    with open("TravelDistanceMap/cities/" + city + ".csv", "w") as file:
        file.write("FIPS,Lng,Lat,Duration,Density\n")
        i = 0
        for county, county_val in counties.items():
                i+=1
                route = get_route(city_pos[0] + "," + city_pos[1] + ";" + county_val[1][0] + "," + county_val[1][1])
                if route["code"] == "NoRoute":
                    continue
                try:
                    print(str(i) + "/" + str(num) + " " + county + " (" + str(county_val[0]) + "): " + str(route["routes"][0]["duration"]))
                except:
                    print(county_val)
                    print(route)
                file.write(county + "," + county_val[1][0] + "," + county_val[1][1] + "," + str(route["routes"][0]["duration"]) + "," + str(county_val[0]) + "\n")
                line = polyline.decode(route["routes"][0]["geometry"])
                for step in line:
                    if step not in steps:
                        steps[step] = 0
                    steps[step] += county_val[0]

    with open("TravelDistanceMap/paths/" + city + ".csv", "w") as pathfile:
        pathfile.write("Lat,Lng,Density\n")
        for step in steps.items():
            pathfile.write(str(step[0][0]) + "," + str(step[0][1]) + "," + str(step[1]) + "\n")

import requests
import csv
from retrying import retry
import polyline

@retry(wait_fixed=5000)
def get_route(coords):
    ans = requests.get("http://router.project-osrm.org/route/v1/driving/" + coords).json()
    if ans is None or ans == {'message': 'Too Many Requests'}:
        raise Exception("Too Many Requests")
    return ans

# teams = []
# i=0
# while True:
#     t = getTBAdata("teams/2018/"+str(i))
#     if len(t)==0:
#         break
#     teams += [team["postal_code"] for team in t if team["country"]=="USA"]
#     print(i)
#     i+=1
#
# zipcodes = {}
# with open("zipcodes.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         zipcode = row["zip"].zfill(5)
#         num = 0
#         for team in teams:
#             if team == zipcode:
#                 num+=1
#         if num > 0:
#             zipcodes[zipcode] = (row["lng"], row["lat"], num)

counties = {}
with open("team_counties.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["FIPS"] not in counties:
            counties[row["FIPS"]] = [0, (row["lng"], row["lat"])]
        counties[row["FIPS"]][0] += 1
print(len(counties))

with open("cities/Philadelphia.csv", "w+") as file, open("paths/Philadelphia.csv", "w+") as pathfile:
    file.write("FIPS,Duration,Density\n")
    pathfile.write("Lat,Lng\n")
    for i, county in enumerate(counties.items(), start=1):
            route = get_route("-75.1253,40.0697;" + county[1][1][0] + "," + county[1][1][1])
            if route["code"] == "NoRoute":
                continue
            print(str(i) + ") " + county[0] + " (" + str(county[1][0]) + "): " + str(route["routes"][0]["duration"]))
            file.write(county[0] + "," + str(route["routes"][0]["duration"]) + "," + str(county[1][0]) + "\n")
            line = polyline.decode(route["routes"][0]["geometry"])
            for step in line:
                pathfile.write(str(step[0]) + "," + str(step[1]) + "\n")

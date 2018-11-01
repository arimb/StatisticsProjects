import requests
import csv
from functions import getTBAdata
from ratelimit import limits, sleep_and_retry
from retrying import retry

@sleep_and_retry
@limits(calls=100, period=60)
@retry
def get_route(coords):
    try:
        ans = requests.get("http://router.project-osrm.org/route/v1/driving/" + coords)

        ans = ans.json()
        if ans is not None:
            return ans
        else:
            print("oops null " + coords)
            return get_route(coords)
    except:
        print("oops " + coords)
        return get_route(coords)

teams = []
i=0
while True:
    t = getTBAdata("teams/2018/"+str(i))
    if len(t)==0:
        break
    teams += [team["postal_code"] for team in t if team["country"]=="USA"]
    print(i)
    i+=1
print(len(teams))
print(teams)

zipcodes = {}
with open("zipcodes.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        zipcode = row["zip"].zfill(5)
        num = 0
        for team in teams:
            if team == zipcode:
                num+=1
        if num > 0:
            zipcodes[zipcode] = (row["lng"], row["lat"], num)
print(len(zipcodes))
print(zipcodes)

tmp = 0
for zipcode in zipcodes.items():
    tmp += zipcode[1][2]
print(tmp)

with open("cities/Philadelphia.csv", "w+") as file:
    for zipcode in zipcodes.items():
            print(zipcode[1][0] + ',' + zipcode[1][1])
            route = get_route("-75.1253,40.0697;" + zipcode[1][0] + "," + zipcode[1][1])
            print(route)
            if route["code"] == "NoRoute":
                continue
            file.write(zipcode[0] + "," + str(route["routes"][0]["duration"]) + "," + str(zipcode[1][2]) + "\n")

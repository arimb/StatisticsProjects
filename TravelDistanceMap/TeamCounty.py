import csv
import math
import sys
from functions import getTBAdata

counties = {}
with open("counties.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        counties[row["FIPS"]] = (float(row["lng"]), float(row["lat"]))

teams = []
with open("teams.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        teams.append((row["team"], float(row["lng"]), float(row["lat"])))

with open("team_counties.csv", "w+") as file:
    file.write("team,FIPS,lng,lat\n")
    for team in teams:
        min = (None, sys.float_info.max)
        for county in counties.items():
            dist = math.sqrt((county[1][0]-team[1])**2 + (county[1][1]-team[2])**2)
            if dist < min[1]:
                min = (county, dist)
        print(team[0] + ": " + min[0][0] + " - " + str(min[1]))
        if min[1] > 4.5:
            print("SKIPPPPPPP ^^^^^")
            continue
        file.write(team[0] + "," + min[0][0] + "," + str(min[0][1][0]) + "," + str(min[0][1][1]) + "\n")

import csv
import json
import math
import sys

counties = {}
with open("TravelDistanceMap/counties.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        counties[row["FIPS"]] = (float(row["lng"]), float(row["lat"]))

with open("TravelDistanceMap/teams.json") as file:
    teams = json.load(file)

with open("TravelDistanceMap/team_counties.csv", "w+") as file:
    file.write("team,FIPS,lng,lat\n")
    for team_key, team_pos in teams.items():
        if None in team_pos.values(): continue
        min = (None, None, 4.5)
        for county_key, county_pos in counties.items():
            dist = math.sqrt((county_pos[0]-team_pos["lng"])**2 + (county_pos[1]-team_pos["lat"])**2)
            if dist < min[2]:
                min = (county_key, county_pos, dist)
        if min[0] is not None:
            print(team_key + ": " + min[0] + " - " + str(min[2]))
            file.write(team_key[0] + "," + min[0] + "," + str(min[1][0]) + "," + str(min[1][1]) + "\n")

import csv
import json
from scipy.spatial import distance
import tbapy

with open('TravelDistanceMap2/all_team_locations_2022.json', 'r') as file:
    tmp_teams = json.load(file)
    all_teams = {}
    for key, team in tmp_teams.items():
        if None in team.values(): continue
        all_teams[key] = (team["lat"], team["lng"])
    del tmp_teams

counties = {}
with open('TravelDistanceMap2/counties.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        counties[row["FIPS"]] = {"Coord": (float(row["lat"]), float(row["lng"])), "Count": 0}

tba = tbapy.TBA('gl4GXuoqG8anLUrLo356LIeeQZk15cfSoXF72YT3mYkI38cCoAmReoCSSF4XWccQ')
current_teams = tba.teams(year=2022, keys=True)

for team_key in current_teams:
    if team_key not in all_teams: continue
    closest = min([(distance.euclidean(county["Coord"], all_teams[team_key]), county_key) for county_key, county in counties.items()])
    if closest[0] < 2:       # 2 degrees of latitude or approx 138 miles
        counties[closest[1]]["Count"] += 1
        print(team_key, closest[1])
    else:
        print(team_key, "not in a county")

counties = {key: val for key, val in counties.items() if val["Count"] > 0}

with open('TravelDistanceMap2/counties.json', 'w') as file:
    json.dump(counties, file)
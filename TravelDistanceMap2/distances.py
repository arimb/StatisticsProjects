import json
import csv
import requests
from retrying import retry
from collections import OrderedDict


@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def get_durations(start_pos, end_pos):
    url = "http://router.project-osrm.org/table/v1/car/" + str(start_pos[1]) + ',' + str(start_pos[0]) + ';' + ';'.join([str(coord[1]) + ',' + str(coord[0]) for coord in end_pos]) + "?sources=0"
    ans = requests.get(url).json()
    if ans is None or ans == {'message': 'Too Many Requests'}:
        raise Exception("Too Many Requests")
    if ans["code"] != "Ok":
        print(ans)
        raise Exception("Error")
    return ans["durations"][0]

conv_center_coords = OrderedDict()
conv_center_duration = OrderedDict()
with open('TravelDistanceMap2/convention_centers.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        conv_center_coords[row['City']] = (row['Lat'], row['Lng'])
        conv_center_duration[row['City']] = {}

with open('TravelDistanceMap2/counties.json', 'r') as f:
    counties = json.load(f)

conv_center_names = list(conv_center_coords.keys())
a = 0
for county_key, county in counties.items():
    print(a, county_key)
    durations = get_durations(county["Coord"], conv_center_coords.values())[1:]
    for i, duration in enumerate(durations):
        if duration is None: continue
        conv_center_duration[conv_center_names[i]][county_key] = duration
    a += 1

with open('TravelDistanceMap2/durations_by_county.csv', 'w+') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['City', *counties.keys()])
    for key, value in conv_center_duration.items():
        writer.writerow([key, *[value[county_key] if county_key in value else 1e9 for county_key in counties.keys()]])
import json
import csv
from matplotlib import projections
import requests
from retrying import retry
from collections import OrderedDict
import pickle
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from math import floor, ceil

# @retry(wait_random_min=1000, wait_random_max=5000)
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
        conv_center_duration[row['City']] = [0, 0]

with open('TravelDistanceMap2/counties.json', 'r') as f:
    counties = json.load(f)
    # county_coords = [x["Coord"] for x in counties.values()]
    # county_qty = [x["Count"] for x in counties.values()]

# conv_center_names = list(conv_center_coords.keys())
# a = 0
# for county_key, county in counties.items():
#     print(a, county_key)
#     durations = get_durations(county["Coord"], conv_center_coords.values())[1:]
#     for i, duration in enumerate(durations):
#         if duration is None: continue
#         conv_center_duration[conv_center_names[i]][0] += duration * county["Count"]
#         conv_center_duration[conv_center_names[i]][1] += county["Count"]
#     with open('TravelDistanceMap2/durations.pkl', 'wb') as f:
#         pickle.dump(conv_center_duration, f)
#     a += 1

with open('TravelDistanceMap2/durations.pkl', 'rb') as f:
    conv_center_duration = pickle.load(f)

conv_center_duration = {key: val[0]/val[1]/3600 for key, val in conv_center_duration.items()}
conv_center_duration = OrderedDict(sorted(conv_center_duration.items(), key=lambda x: x[1]))

# print(conv_center_duration)

with open('TravelDistanceMap2/durations.csv', 'w+') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['City', 'Duration', 'Lat', 'Lng'])
    for key, value in conv_center_duration.items():
        writer.writerow([key, value, conv_center_coords[key][0], conv_center_coords[key][1]])

map = Basemap(projection='merc', llcrnrlat=24, urcrnrlat=53, llcrnrlon=-128, urcrnrlon=-64, resolution='i')
map.drawcoastlines(linewidth=0.25)
map.fillcontinents(color='#cc9966', lake_color='#99ffff')
map.drawmapboundary(fill_color='#99ffff')
map.drawcountries()
map.drawstates(linewidth=0.25, zorder=1)
x,y = map([float(conv_center_coords[key][1]) for key in conv_center_duration.keys()],
          [float(conv_center_coords[key][0]) for key in conv_center_duration.keys()])
# cs = map.contourf(x, y, list(conv_center_duration.values()), levels=10, colors='red', tri=True)
norm = colors.Normalize(list(conv_center_duration.values())[0], list(conv_center_duration.values())[-1])
map.scatter(x, y, c=list(conv_center_duration.values()), s=30, marker='s', cmap='winter_r', norm=norm, edgecolors='k', linewidth=0.5, zorder=999)
plt.colorbar(label='hours', cmap='winter_r', norm=norm, location='bottom', shrink=0.5, pad=0.05, format='%d')
# plt.tricontourf(x, y, list(conv_center_duration.values()), levels=10)

plt.title('Driving Time to US Cities')
plt.show()
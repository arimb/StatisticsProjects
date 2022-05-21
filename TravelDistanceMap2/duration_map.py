import csv
import json
from collections import OrderedDict
from matplotlib import projections
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.colors as colors

DURATION_LIMIT = 10 # hours

durations = OrderedDict()
conv_center_durations = OrderedDict()
with open('TravelDistanceMap2/durations_by_county.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        durations[row['City']] = {key: float(value) for key, value in list(row.items())[1:]}
        conv_center_durations[row['City']] = [0, 0]

conv_center_coords = OrderedDict()
with open('TravelDistanceMap2/convention_centers.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        conv_center_coords[row['City']] = (row['Lat'], row['Lng'])

with open('TravelDistanceMap2/counties.json', 'r') as f:
    counties = json.load(f)


for key, conv_center in durations.items():
    print(key)
    for county_key, duration in conv_center.items():
        if duration < DURATION_LIMIT * 3600:
            conv_center_durations[key][0] += duration * counties[county_key]["Count"]
            conv_center_durations[key][1] += counties[county_key]["Count"]


conv_center_teams = {key: val[1] for key, val in conv_center_durations.items()}
conv_center_teams = OrderedDict(sorted(conv_center_teams.items(), key=lambda x: x[1], reverse=True))
conv_center_durations = {key: val[0]/val[1]/3600 for key, val in conv_center_durations.items()}
conv_center_durations = OrderedDict(sorted(conv_center_durations.items(), key=lambda x: x[1]))

with open('TravelDistanceMap2/durations_limit_{}.csv'.format(DURATION_LIMIT), 'w+') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['City', 'Avg Duration', 'Lat', 'Lng'])
    for key, value in conv_center_durations.items():
        writer.writerow([key, value, conv_center_coords[key][0], conv_center_coords[key][1]])

with open('TravelDistanceMap2/durations_teams_{}.csv'.format(DURATION_LIMIT), 'w+') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['City', 'Teams In Limits', 'Lat', 'Lng'])
    for key, value in conv_center_teams.items():
        writer.writerow([key, value, conv_center_coords[key][0], conv_center_coords[key][1]])

plt.figure()
map = Basemap(projection='merc', llcrnrlat=24, urcrnrlat=53, llcrnrlon=-128, urcrnrlon=-64, resolution='i')
map.drawcoastlines(linewidth=0.25)
map.fillcontinents(color='#cc9966', lake_color='#99ffff')
map.drawmapboundary(fill_color='#99ffff')
map.drawcountries()
map.drawstates(linewidth=0.25, zorder=1)
x,y = map([float(conv_center_coords[key][1]) for key in conv_center_teams.keys()],
          [float(conv_center_coords[key][0]) for key in conv_center_teams.keys()])
norm = colors.Normalize(list(conv_center_teams.values())[0], list(conv_center_teams.values())[-1])
map.scatter(x, y, c=list(conv_center_teams.values()), s=30, marker='s', cmap='winter', norm=norm, edgecolors='k', linewidth=0.5, zorder=999)
plt.colorbar(label='teams', cmap='winter_r', norm=norm, location='bottom', shrink=0.5, pad=0.05, format='%d')
plt.title('FRC Teams Within {} Hours Driving to US Cities'.format(DURATION_LIMIT))
plt.savefig('TravelDistanceMap2/map_teams_{}.png'.format(DURATION_LIMIT))
# plt.show()

plt.figure()
map = Basemap(projection='merc', llcrnrlat=24, urcrnrlat=53, llcrnrlon=-128, urcrnrlon=-64, resolution='i')
map.drawcoastlines(linewidth=0.25)
map.fillcontinents(color='#cc9966', lake_color='#99ffff')
map.drawmapboundary(fill_color='#99ffff')
map.drawcountries()
map.drawstates(linewidth=0.25, zorder=1)
x,y = map([float(conv_center_coords[key][1]) for key in conv_center_durations.keys()],
          [float(conv_center_coords[key][0]) for key in conv_center_durations.keys()])
norm = colors.Normalize(list(conv_center_durations.values())[0], list(conv_center_durations.values())[-1])
map.scatter(x, y, c=list(conv_center_durations.values()), s=30, marker='s', cmap='winter_r', norm=norm, edgecolors='k', linewidth=0.5, zorder=999)
plt.colorbar(label='hours', cmap='winter', norm=norm, location='bottom', shrink=0.5, pad=0.05, format='%d')
plt.title('Avg Driving Time within {} Hours to US Cities'.format(DURATION_LIMIT))
plt.savefig('TravelDistanceMap2/map_limit_{}.png'.format(DURATION_LIMIT))
# plt.show()
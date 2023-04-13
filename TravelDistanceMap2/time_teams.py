import csv
from collections import OrderedDict
import matplotlib.pyplot as plt

DURATION_LIMIT = 10 # hours

teams = OrderedDict()
with open('TravelDistanceMap2/durations_teams_{}.csv'.format(DURATION_LIMIT), 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        teams[row['City']] = int(row['Teams In Limits'])

times = OrderedDict()
with open('TravelDistanceMap2/durations_limit_{}.csv'.format(DURATION_LIMIT), 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        times[row['City']] = float(row['Avg Duration'])


plt.figure()
plt.scatter(times.values(), [teams[city] for city in times.keys()])
for city in times.keys():
    plt.annotate(city, (times[city]+0.02, teams[city]-25), fontsize=8)
plt.xlabel('Average Driving Duration (hours)')
plt.ylabel('Teams In Limits')
plt.title('FRC Teams within {} hours of US City'.format(DURATION_LIMIT))
plt.show()
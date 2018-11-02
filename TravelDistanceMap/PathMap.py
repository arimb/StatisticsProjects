import csv
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(llcrnrlon=-130,llcrnrlat=20,urcrnrlon=-66,urcrnrlat=60,projection='mill')
m.drawcoastlines()
m.drawmapboundary(fill_color='gray')
m.fillcontinents(color='white', zorder=0)
m.drawcountries(linewidth=1.2)
m.drawstates(linewidth=.3)

points = []
with open("paths/Philadelphia.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        points.append((row["lat"], row["lng"]))

points = list(zip(*points))
x, y = m(points[1], points[0])
m.scatter(x, y, 8, color="purple")

plt.show()
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from functions import getTBAdata

m = Basemap(llcrnrlon=-130,llcrnrlat=20,urcrnrlon=-66,urcrnrlat=60,projection='mill')
m.drawcoastlines()
m.drawmapboundary(fill_color='gray')
m.fillcontinents(color='white', zorder=0)
m.drawcountries(linewidth=1.2)
m.drawstates(linewidth=.3)

events = getTBAdata("events/2018")
for event in events:
    if event["event_type"] > 2: continue
    x, y = m(event["lng"], event["lat"])
    m.scatter(x, y, 8, color=["red","blue","#38b9ff"][event["event_type"]])

# x, y = m([-75.1253], [40.0697])
# print(x, y)
# m.scatter([3700000], [1000000], 5, color='blue')
# m.scatter(x, y, 8, color='blue')

plt.show()
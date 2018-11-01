import polyline
import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def getroute(coords):
    try:
        ans = requests.get("http://router.project-osrm.org/route/v1/car/" + coords + "?overview=full").json()
        if ans is not None:
            return ans
        else:
            print("oops null " + coords)
            return getroute(coords)
    except:
        print("oops " + coords)
        return getroute(coords)

m = Basemap(projection='mill',llcrnrlon=-130,llcrnrlat=15,urcrnrlon=-66,urcrnrlat=55)
m.drawcoastlines()
m.drawmapboundary(fill_color='gray')
m.fillcontinents(color='white', zorder=0)
m.drawcountries(linewidth=1.2)
m.drawstates(linewidth=.3)

coords = polyline.decode(getroute("-75.1253,40.0697;-86.1581,39.7684")["routes"][0]["geometry"])
coords = zip(*coords)


x, y = m(coords[1], coords[0])
m.scatter(x, y, 5, marker="--", color="purple", zorder=2)

plt.show()
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='merc', llcrnrlon=-163, llcrnrlat=-180, urcrnrlon=-163, urcrnrlat=180)
map.drawgreatcircle(39.9526, -75.1652, 32.7940, 34.9896)
map.drawcoastlines()
map.fillcontinents()
plt.show()
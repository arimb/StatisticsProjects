import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from functions import getTBAdata

with open("teams.csv") as file:
    allteams = file.readlines()
    teams = {}
    for team in allteams[1:]:
        team = team.strip().split(",")
        teams[team[0]] = (float(team[1]), float(team[2]))


m = Basemap(projection='mill',llcrnrlon=-130,llcrnrlat=15,urcrnrlon=-66,urcrnrlat=55)
# m = Basemap(projection='merc',llcrnrlat=-60,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180)
m.drawcoastlines()
m.drawmapboundary(fill_color='gray')
m.fillcontinents(color='white', zorder=0)
m.drawcountries(linewidth=1.2)
m.drawstates(linewidth=.3)

events = getTBAdata("events/2018")
for event in events:
    if event["event_type"] > 2: continue
    print(event["key"])
    # color = ["red", "blue", "#38b9ff"][event["event_type"]]
    color = ["#ff4444","#33ffff","#f3ae09","#68a429","#6b3232","#727211","#33ccff"][event["week"]]
    # color = "purple"

    teamkeys = getTBAdata("event/"+event["key"]+"/teams/keys")
    for teamkey in teamkeys:
        try:
            m.drawgreatcircle(teams[teamkey[3:]][1], teams[teamkey[3:]][0], event["lng"], event["lat"], linewidth=.3, color=color, zorder=1)
        except:
            pass

    x, y = m(event["lng"], event["lat"])
    m.scatter(x, y, 5, color="purple", zorder=2)

# plt.legend([matplotlib.markers.], ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7"])
plt.show()
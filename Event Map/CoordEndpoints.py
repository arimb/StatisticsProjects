from functions import getTBAdata

with open("teams.csv") as file:
    allteams = file.readlines()
    teams = {}
    for team in allteams[1:]:
        team = team.strip().split(",")
        teams[team[0]] = (float(team[1]), float(team[2]))

file = open("coord_endpoints.csv", "w+")
file.write("TeamLat,TeamLng,EventLat,EventLng\n")

events = getTBAdata("events/2019")
for event in events:
    if event["event_type"] > 2: continue
    print(event["key"])

    teamkeys = getTBAdata("event/" + event["key"] + "/teams/keys")
    for teamkey in teamkeys:
        try:
            file.write(str(teams[teamkey[3:]][1]) + "," + str(teams[teamkey[3:]][0]) + "," + str(event["lng"]) + "," + str(event["lat"]) + "," +str(event["event_type"]) + "\n")
        except:
            pass

file.close()
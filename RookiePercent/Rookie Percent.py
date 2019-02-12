from functions import getTBAdata

years = range(2002, 2020)
all_events = []

for year in years:
    events = getTBAdata("events/" + str(year) + "/keys")
    for event in events:
        print(event)
        teams = getTBAdata("event/" + event + "/teams")
        if len(teams) == 0:
            continue
        rookie = sum([1 if t["rookie_year"]==year else 0 for t in teams])
        all_events.append((event, rookie, len(teams)))

all_events = sorted(all_events, key=lambda x:x[1]/x[2], reverse=True)
print(all_events)
with open("rookie_percent.csv", "w+") as file:
    file.write("Event,Rookies,Total,% Rookies\n")
    for e in all_events:
        file.write(e[0] + "," + str(e[1]) + "," + str(e[2]) + "," + str(e[1]/e[2]) + "\n")
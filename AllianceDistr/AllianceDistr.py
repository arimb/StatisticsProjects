from functions import getTBAdata
import traceback

years = range(2010, 2020)
data = {y:[0]*8 for y in years}
for year in years:
    print(year)
    events = getTBAdata("events/" + str(year))
    for event in events:
        if event["event_type"]>5 or len(event["division_keys"])>0: continue
        alliances = getTBAdata("event/" + event["key"] + "/alliances")
        print(event["key"])
        if alliances is None: continue
        for i, a in enumerate(alliances):
            try:
                if a["status"] == "unknown": continue
                if a["status"]["level"] == "f":
                    try:
                        print(i+1)
                        data[year][i] += 1
                    except:
                        traceback.print_exc()
                        print(a)
            except:
                traceback.print_exc()
                print(a)

with open("finals.csv", "w+") as file:
    file.write("Year," + ",".join([str(x) for x in range(1,9)]) + "\n")
    for year, alliances in data.items():
        file.write(str(year) + ",")
        for a in alliances:
            file.write(str(a) + ",")
        file.write("\n")
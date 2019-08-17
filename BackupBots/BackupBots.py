from functions import get_tba_data

data = {}

for year in range(2014,2020):
    tmp = [0, 0]
    events = get_tba_data("events/" + str(year) + "/simple")
    for event in events:
        if event["event_type"] not in [0, 1, 2, 5]: continue
        print(event["key"])
        alliances = get_tba_data("event/" + event["key"] + "/alliances")
        if alliances is None: continue
        for alliance in alliances:
            try:
                if alliance is None: continue
                if alliance["backup"] is not None: tmp[0] += 1
                tmp[1] += 1
            except KeyError:
                pass
    try:
        data[year] = tmp
        print(data[year])
    except ZeroDivisionError:
        print("no alliances in " + str(year) + " :(")

print(data)
print({year:x[0]/x[1] for year, x in data.items()})
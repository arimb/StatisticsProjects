from functions import getTBAdata

def getregion(teamKey):
    team = getTBAdata("team/" + teamKey + "/simple")
    districts = getTBAdata("team/" + teamKey + "/districts")
    if len(districts) != 0:
        return districts[0]["abbreviation"].upper()
    elif team["country"] not in ["USA", "Canada"]:
        return team["country"]
    else:
        return team["state_prov"]


years = range(2010, 2019)
regions = {}

for year in years:
    print(year)
    cmp_awards = []
    events = getTBAdata("events/"+str(year))
    for event in events:
        if event["event_type"] in [3, 4]:
            print(event["key"])
            awards = getTBAdata("event/"+event["key"]+"/awards")
            for award in awards:
                if award["award_type"] in [0, 9, 10, 69]:
                    for recipient in award["recipient_list"]:
                        if recipient["team_key"] not in cmp_awards:
                            cmp_awards.append(recipient["team_key"])
    print(cmp_awards)
    yearly = {}
    for teamKey in cmp_awards:
        region = getregion(teamKey)
        if region not in yearly:
            yearly[region] = 0
        yearly[region] += 1
    for region in yearly:
        if region not in regions:
            regions[region] = []
        regions[region].append((year, yearly[region]))

print(regions)
with open("region_award_competitiveness.csv", "w+") as file:
    file.write("Region,")
    for year in years:
        file.write(str(year) + ",")
    file.write("\n")
    for region in regions:
        regions[region] = dict(regions[region])
        print(region + ": " + str(regions[region]))
        file.write(region + ",")
        for year in years:
            try:
                file.write(str(regions[region][year]) + ",")
            except KeyError:
                file.write(",")
        file.write("\n")



#     for event in events:
#         if event["event_type"] in [0, 2]:
#             print(event["key"])
#             cmp = 0
#             local = 0
#             teams = getTBAdata("event/" + event["key"] + "/teams/keys")
#             for team in teams:
#                 if team in cmp_awards:
#                     cmp += 1
#             awards = getTBAdata("event/" + event["key"] + "/awards")
#             for award in awards:
#                 if award["award_type"] in [0, 9, 10, 69]:
#                     for recipient in award["recipient_list"]:
#                         local += 1
#             cmp /= local
#             if event["name"] not in regionals:
#                 regionals[event["name"]] = []
#             regionals[event["name"]].append((year, cmp))
#     print(regionals)
#
# with open("region_award_competitiveness.csv", "w+") as file:
#     file.write("event,")
#     for year in years:
#         file.write(str(year) + ",")
#     file.write("\n")
#     for event in regionals:
#         regionals[event] = dict(regionals[event])
#         print(event + ": " + str(regionals[event]))
#         file.write(event + ",")
#         for year in years:
#             try:
#                 file.write(str(regionals[event][year]) + ",")
#             except KeyError:
#                 file.write(",")
#         file.write("\n")
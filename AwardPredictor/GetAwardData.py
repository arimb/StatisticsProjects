from functions import getTBAdata

award_number = {0 : "CHAIRMANS",
                1 : "WINNER",
                2 : "FINALIST",
                9 : "ENGINEERING_INSPIRATION",
                11 : "GRACIOUS_PROFESSIONALISM",
                13 : "JUDGES",
                16 : "INDUSTRIAL_DESIGN",
                17 : "QUALITY",
                18 : "SAFETY",
                20 : "CREATIVITY",
                21 : "ENGINEERING_EXCELLENCE",
                22 : "ENTREPRENEURSHIP",
                23 : "EXCELLENCE_IN_DESIGN",
                27 : "IMAGERY",
                29 : "INNOVATION_IN_CONTROL",
                30 : "SPIRIT",
                31 : "WEBSITE"}

with open("output.txt", "w+") as file:
    file.write("data = {\n")

    teams = {}
    i = 0
    while True:
        tmp = getTBAdata("teams/2018/" + str(i) + "/keys")
        if len(tmp)==0: break
        for team in tmp:
            print(team)
            awards = getTBAdata("team/" + team + "/awards")
            teams[team] = {"WINNER" : [],
                           "FINALIST" : [],
                           "CHAIRMANS" : [],
                           "ENGINEERING_INSPIRATION" : [],
                           "CREATIVITY" : [],
                           "ENGINEERING_EXCELLENCE" : [],
                           "INDUSTRIAL_DESIGN" : [],
                           "INNOVATION_IN_CONTROL" : [],
                           "QUALITY" : [],
                           "ENTREPRENEURSHIP" : [],
                           "IMAGERY" : [],
                           "JUDGES" : [],
                           "GRACIOUS_PROFESSIONALISM" : [],
                           "SAFETY" : [],
                           "SPIRIT" : []}
            for award in awards:
                try:
                    if award_number[award["award_type"]] in teams[team]:
                        if award["year"] not in teams[team][award_number[award["award_type"]]]:
                            teams[team][award_number[award["award_type"]]].append(award["year"])
                except KeyError: pass
            file.write("\"" + str(team) + "\" : " + str(teams[team]) + ",\n")
        i += 1
    file.write("\n}")
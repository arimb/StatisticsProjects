from functions import getTBAdata

file = open("team_age.csv", "w+")
file.write("Team #,Region,Age\n")
i=0
teams = getTBAdata("teams/2018/"+str(i))
while len(teams)>0:
    print(i)
    for team in teams:
        print(team["key"])
        districts = getTBAdata("team/"+team["key"]+"/districts")
        if len(districts) != 0:
            region = districts[0]["abbreviation"].upper()
        elif team["country"] != "USA":
            region = team["country"]
        else:
            region = team["state_prov"]

        file.write(str(team["team_number"]) + "," + region + "," + str(2019-team["rookie_year"]) + "\n")
    i+=1
    teams = getTBAdata("teams/2018/"+str(i))
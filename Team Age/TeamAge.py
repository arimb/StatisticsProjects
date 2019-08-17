from functions import get_tba_data

year = 2019

file = open("team_age.csv", "w+")
file.write("Team #,Region,Age\n")
i=0
while True:
    teams = get_tba_data("teams/" + str(year) + "/" + str(i))
    if len(teams)==0: break
    print(i)
    for team in teams:
        print(team["key"])
        districts = get_tba_data("team/"+team["key"]+"/districts")
        if len(districts) != 0:
            region = districts[0]["abbreviation"].upper()
        elif team["country"] != "USA":
            region = team["country"]
        else:
            region = team["state_prov"]

        file.write(str(team["team_number"]) + "," + region + "," + str(year+1-team["rookie_year"]) + "\n")
    i+=1
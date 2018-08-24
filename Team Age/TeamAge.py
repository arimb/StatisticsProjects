import requests

def getdata(url):
    try:
        ans = requests.get(url, "accept=application%2Fjson&X-TBA-Auth-Key=gl4GXuoqG8anLUrLo356LIeeQZk15cfSoXF72YT3mYkI38cCoAmReoCSSF4XWccQ").json()
        if ans is not None:
            return ans
        else:
            print("oops null " + url)
            getdata(url)
    except:
        print("oops " + url)
        getdata(url)

file = open("team_age.csv", "w+")
file.write("Team #,Region,Age\n")
i=0
teams = getdata("https://www.thebluealliance.com/api/v3/teams/2018/"+str(i))
while len(teams)>0:
    print(i)
    for team in teams:
        print(team["key"])
        districts = getdata("https://www.thebluealliance.com/api/v3/team/"+team["key"]+"/districts")
        if len(districts) != 0:
            region = districts[0]["abbreviation"].upper()
        elif team["country"] != "USA":
            region = team["country"]
        else:
            region = team["state_prov"]

        file.write(str(team["team_number"]) + "," + region + "," + str(2019-team["rookie_year"]) + "\n")
    i+=1
    teams = getdata("https://www.thebluealliance.com/api/v3/teams/2018/"+str(i))
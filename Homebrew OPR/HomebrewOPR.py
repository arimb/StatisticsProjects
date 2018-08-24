import requests
import statsmodels.api as sm

def getdata(url):
    try:
        ans = requests.get("https://www.thebluealliance.com/api/v3/" + url, "accept=application%2Fjson&X-TBA-Auth-Key=gl4GXuoqG8anLUrLo356LIeeQZk15cfSoXF72YT3mYkI38cCoAmReoCSSF4XWccQ").json()
        if ans is not None:
            return ans
        else:
            print("oops null " + url)
            getdata(url)
    except:
        print("oops " + url)
        getdata(url)

eventKey = input("Event Key: ")
teams = getdata("event/"+eventKey+"/teams/keys")

matrix = []
scores = []
matches = getdata("event/"+eventKey+"/matches/simple")
for match in matches:
    for alliance in [match["alliances"]["red"], match["alliances"]["blue"]]:
        tmp = [0] * len(teams)
        for team in alliance["team_keys"]:
            tmp[teams.index(team)] = 1
        matrix.append(tmp)
        scores.append(alliance["score"])
    tmp = [0] * len(teams)
    for team in match["alliances"]["red"]["team_keys"]:
        tmp[teams.index(team)] = 1
    for team in match["alliances"]["blue"]["team_keys"]:
        tmp[teams.index(team)] = -1
    matrix.append(tmp)
    scores.append(match["alliances"]["red"]["score"] - match["alliances"]["blue"]["score"])

results = sm.OLS(scores, matrix).fit()
print(list(zip(teams, results.params)))

import statsmodels.api as sm
from functions import getTBAdata

eventKey = input("Event Key: ")
teams = getTBAdata("event/"+eventKey+"/teams/keys")

matrix = []
scores = []
matches = getTBAdata("event/"+eventKey+"/matches/simple")
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

import requests

def getdata(url):
    try:
        return requests.get(url, "accept=application%2Fjson&X-TBA-Auth-Key=gl4GXuoqG8anLUrLo356LIeeQZk15cfSoXF72YT3mYkI38cCoAmReoCSSF4XWccQ").json()
    except:
        print("oops " + url)
        getdata(url)

class Team:
    def __init__(self, status):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.add_event(status)

    def add_event(self, status):
        print(status)
        if status is not None:
            if status["qual"] is not None:
                if status["qual"]["ranking"] is not None:
                    if status["qual"]["ranking"]["record"] is not None:
                        self.wins += status["qual"]["ranking"]["record"]["wins"]
                        self.ties += status["qual"]["ranking"]["record"]["ties"]
                        self.losses += status["qual"]["ranking"]["record"]["losses"]
            if status["playoff"] is not None:
                if status["playoff"]["record"] is not None:
                    self.wins += status["playoff"]["record"]["wins"]
                    self.ties += status["playoff"]["record"]["ties"]
                    self.losses += status["playoff"]["record"]["losses"]

teams = {}
file = open("winning_season.csv", "w+")

events = getdata("https://www.thebluealliance.com/api/v3/events/2018")
for event in events:
    if 0 <= event["event_type"] <= 3 or event["event_type"] == 5:
        if len(event["division_keys"]) == 0:
            print(event["key"])
            statuses = getdata("https://www.thebluealliance.com/api/v3/event/"+str(event["key"])+"/teams/statuses")
            for teamKey in statuses:
                if teamKey in teams:
                    teams[teamKey].add_event(statuses[teamKey])
                else:
                    teams[teamKey] = Team(statuses[teamKey])

file.write("Team,Wins,Losses,Ties,Ratio\n")
for teamKey in teams:
    print(teamKey)
    file.write(teamKey[3:] + "," + str(teams[teamKey].wins) + "," + str(teams[teamKey].losses) + "," + str(teams[teamKey].ties) + "," + ("99999" if teams[teamKey].losses == 0 else str(teams[teamKey].wins/teams[teamKey].losses)) + "\n")
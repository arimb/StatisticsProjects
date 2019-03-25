from functions import getTBAdata
from numpy import count_nonzero

lookup = [16, 17, 20, 21, 29, 71]
names = ["IndDsn","Qual","Creativ","EngEx","Cntrl","Auton"]

teams = []
hexafecta = {}
quinfecta = {}
all_teams = {}
i = 0
while True:
    tmp = getTBAdata("teams/" + str(i) + "/keys")
    if len(tmp)==0: break
    teams = teams + tmp
    print(i)
    i += 1


for team in teams:
    print(team)
    awards = getTBAdata("team/" + team + "/awards")
    hex = [0, 0, 0, 0, 0, 0]
    for award in awards:
        try:
            hex[lookup.index(award["award_type"])] += 1
        except ValueError:
            pass
    if count_nonzero(hex) == 6: hexafecta[team] = hex
    elif count_nonzero(hex) == 5: quinfecta[team] = hex
    all_teams[team] = hex

with open("hexafecta.csv", "w+") as file:
    file.write("Team,"+",".join(names)+"\n")
    for team, awards in hexafecta.items():
        file.write(team + "," + ",".join([str(a) for a in awards]) + "\n")

with open("quinfecta.csv", "w+") as file:
    file.write("Team,"+",".join(names)+"\n")
    for team, awards in quinfecta.items():
        file.write(team + "," + ",".join([str(a) for a in awards]) + "\n")

with open("all_teams.csv", "w+") as file:
    file.write("Team,"+",".join(names)+"\n")
    for team, awards in all_teams.items():
        file.write(team + "," + ",".join([str(a) for a in awards]) + "\n")
import math

counties = {}
with open("C:/Users/Ari/Documents/Robotics/StatisticsProjects/TravelDistanceMap/counties.csv") as file:
    allcounties = file.readlines()
titles = allcounties[0].strip().split(",")
for county in allcounties[1:]:
    county = county.strip().split(",")
    counties[int(county[0])] = {}
    for i, element in enumerate(county[1:], start=1):
        counties[int(county[0])][titles[i]] = float(element)

teams = []
with open("C:/Users/Ari/Documents/Robotics/StatisticsProjects/TravelDistanceMap/teams.csv") as file:
    allteams = file.readlines()
for team in allteams[1:]:
    team = team.strip().split(",")
    tmp = {}
    for i, element in enumerate(team[1:], start=1):
        tmp[titles[i]] = float(element)
    teams.append(tmp)

distances = {}
for county in counties:
    print(county)
    countydist = []
    for team in teams:
        countydist.append(3959*math.acos(math.sin(teams[team]["lat"])*math.sin(counties[county]["lat"]) +
                          math.cos(teams[team]["lat"])*math.cos(counties[county]["lat"])*
                          math.cos(abs(teams[team]["lng"]-counties[county]["lng"]))))
    distances[county] = countydist

with open("C:/Users/Ari/Documents/Robotics/StatisticsProjects/TravelDistanceMap/1.csv") as file:
    file.write("Team,")
    distances = list(distances.items())
    for team,value in distances:
        file.write(str())
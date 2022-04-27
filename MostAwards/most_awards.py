import tbapy
tba = tbapy.TBA('gl4GXuoqG8anLUrLo356LIeeQZk15cfSoXF72YT3mYkI38cCoAmReoCSSF4XWccQ')

award_type = [27]   # imagery award key
data = []

teams = tba.teams(keys=True)
print(len(teams))
for team in teams:
    print(team)
    awards = tba.team_awards(team)
    data.append((sum([1 if award['award_type'] in award_type else 0 for award in awards]), team))

data.sort(reverse=True)
print(data[0][1])
print(data)

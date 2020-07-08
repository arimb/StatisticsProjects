import csv

users = []
with open('users.csv') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        users.append({'username': row[0],
                      'days': int(row[1]),
                      'group': int(row[2]),
                      'team': row[3],
                      'elo': row[4]})

teams = {}
for user in users:
    if user['team'] not in teams:
        teams[user['team']] = {0: 0,
                               1: 0,
                               2: 0,
                               3: 0,
                               4: 0,
                               5: 0,
                               'elo': user['elo']}
    for i in range(0, user['group']+1):
        teams[user['team']][i] += 1

with open('teams.csv', 'w+') as file:
    file.write('Team #,0,1,2,3,4,5,Elo\n')
    for num, team in teams.items():
        file.write(num + ',')
        for i in range(0, 6):
            file.write(str(team[i]) + ',')
        file.write(team['elo'] + '\n')

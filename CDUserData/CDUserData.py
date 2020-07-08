import json
import csv
import requests

def get_team(username, retries=0):
    try:
        ans = requests.get('https://www.chiefdelphi.com/users/' + username + '.json').json()
        return ans['user']['user_fields']['1']
    except:
        print("oops " + username)
        if retries > 1:
            return None
        else:
            return get_team(username, retries+1)

def get_users(page):
    try:
        ans = requests.get('https://www.chiefdelphi.com/directory_items.json?period=yearly&order=days_visited&page=' + str(page)).json()['directory_items']
        return ans
    except:
        print("oops " + page)
        return get_users(page)

def group(days):
    if days < 25:
        return 0
    elif days <= 80:
        return 1
    elif days <= 150:
        return 2
    elif days <= 220:
        return 3
    elif days <= 290:
        return 4
    else:
        return 5

elos = {}
with open('elos.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        elos[row[0]] = row[1]


page = 0
flag = False
while True:
    print(page)
    users = []
    users_raw = get_users(page)

    for user in users_raw:
        if user['days_visited'] < 2:
            flag = True
            break
        name = user['user']['username']
        team = get_team(name)
        if team is not None and team in elos:
            users.append({'username': name,
                          'days': str(user['days_visited']),
                          'group': str(group(user['days_visited'])),
                          'team': team,
                          'elo': elos[team]})
        else:
            users.append({'username': name,
                          'days': str(user['days_visited']),
                          'group': str(group(user['days_visited'])),
                          'team': '',
                          'elo': ''})
        print(users[-1])

    if flag:
        break

    with open('users.csv', 'a') as file:
##        file.write('User,Days Visited,Group,Team #,Elo\n')
        for user in users:
            file.write(user['username'] + ',' +
                       user['days'] + ',' +
                       user['group'] + ',' +
                       user['team'] + ',' +
                       user['elo'] + '\n')

    page += 1

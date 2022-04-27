import json
import csv
import requests

def get_team(username, retries=0):
    try:
        ans = requests.get('https://www.chiefdelphi.com/users/' + username + '.json').json()
        return ans['user']['user_fields']['1'], ans['user']['user_fields']['2']
    except:
        print("oops " + username)
        if retries > 1:
            return None, None
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

with open('users.csv', 'w+') as file:
    file.write('User,Team #,Rookie Year,Likes Recieved,Likes Given,Topics,Replies,Viewed,Read,Visits,Elo\n')

page = 0
flag = False
while True:
    print(page)
    users = []
    users_raw = get_users(page)

    for user in users_raw:
        if user['days_visited'] < 1:
            flag = True
            break
        name = user['user']['username']
        team, rookie = get_team(name)
        users.append({'username': name,
                      'team': str(team),
                      'rookie': str(rookie),
                      'likes_received': str(user['likes_received']),
                      'likes_given': str(user['likes_given']),
                      'topics': str(user['topic_count']),
                      'replies': str(user['post_count']),
                      'viewed': str(user['topics_entered']),
                      'read': str(user['posts_read']),
                      'days': str(user['days_visited']),
                      'elo': (elos[team] if team in elos else '')})
        print(users[-1])

    if flag:
        break

    with open('users.csv', 'a') as file:
        for user in users:
            file.write(user['username'] + ',' +
                       user['team'] + ',' +
                       user['rookie'] + ',' +
                       user['likes_received'] + ',' +
                       user['likes_given'] + ',' +
                       user['topics'] + ',' +
                       user['replies'] + ',' +
                       user['viewed'] + ',' +
                       user['read'] + ',' +
                       user['days'] + ',' +
                       user['elo'] + '\n')

    page += 1

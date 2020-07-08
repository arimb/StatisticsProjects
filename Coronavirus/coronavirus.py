from functions import get_tba_data

cancelled = ["2020orsal",
             "2020orwil",
             "2020pncmp",
             "2020waahs",
             "2020waamv",
             "2020wabel",
             "2020waspo",
             "2020wayak",
             "2020mrcmp",
             "2020njbri",
             "2020njfla",
             "2020njrob",
             "2020njski",
             "2020njtab",
             "2020paben",
             "2020paphi",
             "2020mial2",
             "2020mialp",
             "2020mibel",
             "2020micen",
             "2020micmp",
             "2020midet",
             "2020miesc",
             "2020mifer",
             "2020migul",
             "2020miken",
             "2020milak",
             "2020milan",
             "2020milin",
             "2020miliv",
             "2020mimar",
             "2020mimid",
             "2020mimus",
             "2020mishe",
             "2020mitry",
             "2020miwmi",
             "2020miwoo",
             '2020isde3',
             '2020isde4',
             '2020iscmp',
             "2020gaalb",
             "2020gacar",
             "2020gacmp",
             "2020gacol",
             "2020ftcmp",
             '2020txama',
             '2020txfor',
             '2020txnew',
             "2020chcmp",
             "2020mdedg",
             "2020mdowi",
             "2020vabla",
             "2020vapor",
             '2020onto1',
             '2020onott',
             '2020bexi',
             '2020bexi2',
             '2020chta',
             '2020azfl',
             '2020ausc',
             '2020nytr',
             '2020casd',
             '2020casf',
             '2020cafr',
             '2020nyro',
             '2020flor',
             '2020mosl',
             '2020okok',
             '2020nyut',
             '2020ausp',
             '2020nyli',
             '2020nyli2',
             '2020nysu',
             '2020paca',
             '2020tnme',
             '2020cave',
             '2020tnkn',
             '2020casj',
             '2020azpx',
             '2020qcmo'
             ]

missing = [0]*5
attending = [0]*5
district = [0]*5
teams = []

for event in cancelled:
    print(event)
    for team in get_tba_data('event/' + event + '/teams/keys'):
        if not team[:3]=='frc': print('AHHHHHH')
        if team not in teams:
            teams.append(team)
print(len(teams))

for team in sorted(teams):
    print(team)
    events = [x for x in get_tba_data('team/' + team + '/events/2020/simple') if x['event_type']<2]
    num = len(events)
    tmp = 0
    flag = False
    for event in events:
        if event['key'] in cancelled:
            tmp +=1
        if event['event_type']==1:
            flag = True
    missing[tmp] += 1
    attending[num-tmp] += 1
    if flag:
        district[num-tmp] += 1

print(missing)
print(attending)
print(district)
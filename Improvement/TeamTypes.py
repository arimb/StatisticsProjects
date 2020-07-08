from functions import get_tba_data
import pickle

year = 2017

# all_teams = {}
# districts = [x['key'] for x in get_tba_data('districts/' + str(year))]
# for district in districts:
#     print(district)
#     teams = get_tba_data('district/' + district + '/teams/keys')
#     for team in teams:
#         all_teams[team] = [[], 0]
#
# # for e in get_tba_data('events/' + str(year)):
# #     print(e)
# #     print(e['week'])
# # events = [x if x['week'] is not None else  for x in get_tba_data('events/' + str(year))]#.sort(key=lambda x: x['week'])
# events = get_tba_data('events/' + str(year))
# for e in events:
#     if e['week'] is None: e['week'] = 10
# events.sort(key=lambda x: x['week'])
# print(events)
# for event in events:
#     if len(event['division_keys']) != 0: continue
#     event_type = {1:1, 2:2, 3:3, 5:2}.get(event['event_type'], None)
#     if event_type not in [1,2,3]: continue
#     print(event['key'])
#     teams = get_tba_data('event/' + event['key'] + '/oprs')['oprs']
#     for team, opr in teams.items():
#         if team not in all_teams: continue
#         all_teams[team][0].append(opr)
#         all_teams[team][1] = max(all_teams[team][1], event_type)
#
# with open('data.pkl', 'wb') as file:
#     pickle.dump(all_teams, file)

with open('data.pkl', 'rb') as file:
    all_teams = pickle.load(file)

with open('results.csv', 'w+') as file:
    file.write('Team,Type,Event1,Event2,Event3,Event4,Event5\n')
    team_list = sorted(list(all_teams.items()), key=lambda x:x[1][1])
    for team in team_list:
        file.write(team[0] + ',' + str(team[1][1]) + ',')
        for e in team[1][0]:
            file.write(str(e) + ',')
        file.write('\n')
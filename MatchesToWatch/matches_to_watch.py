from functions import get_tba_data
import csv

week = 1
all_matches = []

with open('elo.csv') as f:
    reader = csv.reader(f)
    elo = [(x[0], int(x[1])) for x in list(reader)]

events = get_tba_data('events/2020')
for event in events.filter(lambda x: x['week'] == week):
    matches = get_tba_data('event/' + event['key'] + '/matches/simple')
    for match in matches:
        match['alliances']['red']['']
import tbapy
import matplotlib.pyplot as plt
import pickle

def level(alliance):
    if alliance is None:
        return []
    elif alliance['status'] == 'unknown':
        return []
    elif alliance['status']['status'] == 'won':
        return [1,2,3,4]
    elif alliance['status']['level'] == 'f':
        return [2,3,4]
    elif alliance['status']['level'] == 'sf':
        return [3,4]
    elif alliance['status']['level'] == 'qf':
        return [4]
    else:
        return []

tba = tbapy.TBA('n7Dnypajo6tcZ5Io6nxG6PzsxfoRAMuBPiHIWnUb1n2KvWAaujDboTt0ZDrQVXlR')

year = 2015
events = tba.events(2022, simple=True)

data = {1: {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0},
        2: {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0},
        3: {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0},
        4: {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0},
        0: {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}}
names = {1: "Winners", 2: "Finals", 3: "Semifinals", 4: "Quarterfinals"}

for event in events:
    if event['event_type'] not in [0,1,2,3]:
        continue
    print(event['key'])
    try:
        alliances = tba.event_alliances(event['key'])
    except TypeError:
        continue
    for num, alliance in enumerate(alliances, start=1):
        for i in level(alliance):
            if 'name' in alliance.keys():
                data[i][alliance['name'][-1]] += 1
            else:
                data[i][num] += 1

# with open('data_save.pickle', 'wb') as f:
#     pickle.dump(data, f)

# with open('data_save.pickle', 'rb') as f:
#     data = pickle.load(f)

for i in [1,2,3,4]:
    # fig, ax = plt.figure()
    fig, ax = plt.subplots()
    bars = plt.bar(data[i].keys(), data[i].values(), align='center')
    ax.bar_label(bars)
    plt.title(names[i])
    plt.xlabel('Alliance')
    plt.ylabel('Number of Occurances')
    plt.savefig(f'{year}_{names[i]}.png')
plt.show()

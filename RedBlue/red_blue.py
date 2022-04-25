import tbapy
from scipy import stats
import pickle

tba = tbapy.TBA('gl4GXuoqG8anLUrLo356LIeeQZk15cfSoXF72YT3mYkI38cCoAmReoCSSF4XWccQ')

winners = [0,0,0]

# events = tba.events(year=2022, simple=True)
# for event in events:
#     if event["event_type"] > 5: continue
#     print(event["key"])
#     matches = tba.event_matches(event=event["key"], simple=True)
#     for match in matches:
#         if match["comp_level"] != "qm": continue
#         winners[{"red":0, "blue":1, "":2}[match["winning_alliance"]]] += 1

# with open('RedBlue/pickle.pkl', 'wb') as f:
#     pickle.dump(winners, f)

with open('RedBlue/pickle.pkl', 'rb') as f:
    winners = pickle.load(f)

total = sum(winners)
print(winners)
print(total)

results = stats.chisquare(winners[0:2])
print(results.pvalue)
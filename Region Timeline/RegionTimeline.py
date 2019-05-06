from functions import get_tba_data

def getregion(team):
    abv_table = {"AL": "Alabama",
                 "AK": "Alaska",
                 "AZ": "Arizona",
                 "AR": "Arkansas",
                 "CA": "California",
                 "CO": "Colorado",
                 "CT": "Connecticut",
                 "DE": "Delaware",
                 "FL": "Florida",
                 "GA": "Georgia",
                 "HI": "Hawaii",
                 "ID": "Idaho",
                 "IL": "Illinois",
                 "IN": "Indiana",
                 "IA": "Iowa",
                 "KS": "Kansas",
                 "KY": "Kentucky",
                 "LA": "Louisiana",
                 "ME": "Maine",
                 "MD": "Maryland",
                 "MA": "Massachusetts",
                 "MI": "Michigan",
                 "MN": "Minnesota",
                 "MS": "Mississippi",
                 "MO": "Missouri",
                 "MT": "Montana",
                 "NE": "Nebraska",
                 "NV": "Nevada",
                 "NH": "New Hampshire",
                 "NJ": "New Jersey",
                 "NM": "New Mexico",
                 "NY": "New York",
                 "NC": "North Carolina",
                 "ND": "North Dakota",
                 "OH": "Ohio",
                 "OK": "Oklahoma",
                 "OR": "Oregon",
                 "PA": "Pennsylvania",
                 "RI": "Rhode Island",
                 "SC": "South Carolina",
                 "SD": "South Dakota",
                 "TN": "Tennessee",
                 "TX": "Texas",
                 "UT": "Utah",
                 "VT": "Vermont",
                 "VA": "Virginia",
                 "WA": "Washington",
                 "WV": "West Virginia",
                 "WI": "Wisconsin",
                 "WY": "Wyoming",
                 "ON": "Ontario",
                 "QC": "Quebec",
                 "NS": "Nova Scotia",
                 "NB": "New Brunswick",
                 "MB": "Manitoba",
                 "BC": "British Columbia",
                 "PE": "Prince Edward Island",
                 "SK": "Saskatchewan",
                 "AB": "Alberta",
                 "NL": "Newfoundland and Labrador",
                 "PR": "Puerto Rico",
                 "DC": "District of Columbia"}
    # districts = getdata("team/" + team["key"] + "/districts")
    # if len(districts) != 0:
    #     return districts[0]["abbreviation"].upper()
    if team["country"] not in ["USA", "Canada"]:
        return team["country"]
    else:
        if team["state_prov"] in abv_table:
            return abv_table[team["state_prov"]]
        else:
            return team["state_prov"]


years = range(1992, 2019)
regions = {}

for year in years:
    print(year)
    page = 0
    yearly = {}
    while True:
        teams = get_tba_data("teams/" + str(year) + "/" + str(page) + "/simple")
        if len(teams) == 0:
            break
        for team in teams:
            print(team["key"])
            region = getregion(team)
            if region not in yearly:
                yearly[region] = 0
            yearly[region] += 1
        page += 1
    for region in yearly:
        if region not in regions:
            regions[region] = []
        regions[region].append((year, yearly[region]))

print(regions)
with open("region_timeline_2019.csv", "w+") as file:
    file.write("Region,")
    for year in years:
        file.write(str(year) + ",")
    file.write("\n")
    for region in regions:
        regions[region] = dict(regions[region])
        try:
            print(region + ": " + str(regions[region]))
            file.write(region + ",")
            for year in years:
                try:
                    file.write(str(regions[region][year]) + ",")
                except KeyError:
                    file.write("0,")
            file.write("\n")
        except TypeError:
            pass

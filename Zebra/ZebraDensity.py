import csv
import os

dirpath = "C:\Users\Ari\Documents\Robotics\StatisticsProjects\Zebra\Files"
for match in os.listdir(dirpath):
    num = match[5:]
    for team in os.listdir(dirpath+"/"+match):
        tnum =  team[:team.index('_')]

        with open(dirpath+"/"+match+"/"+team) as csvfile:
            points = []
            reader = csv.reader(csvfile)
            for row in reader[1:]:
                tmp = row.split(",")
                points.append((tmp[0], tmp[1]))

            
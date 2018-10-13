import csv
import os
import math

scale = 2
dirpath = "Files"
red = [[0]*27 for i in range(54)]

for match in os.listdir(dirpath):
    mnum = match[5:]
    for team in os.listdir(dirpath+"/"+match):
        tnum =  team[:team.index('_')]
        print(mnum + ', ' + tnum)

        with open(dirpath+"/"+match+"/"+team) as csvfile:
            points = []
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                points.append((float(row[0]), float(row[1])))

            redblue = points[0][0] < 27
            for y in range(27):
                for x in range(54):
                    red[x if redblue else 53-x][y if redblue else 26-y] += sum([1 if math.sqrt((x-p[0])**2+(y-p[1])**2)<scale else 0 for p in points])/len(points)

with open("red.csv", "w+") as file:
    for y in range(27):
        for x in range(54):
            file.write(str(x) + "," + str(y) + "," + str(red[x][y]) + "\n")
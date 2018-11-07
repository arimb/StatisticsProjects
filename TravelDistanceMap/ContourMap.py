import gmplot
import csv

points = []
with open("C:/Users/arimb/Desktop/Indianapolis.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        points.append((float(row["Lat"]), float(row['Lng']), int(row["Density"])))

gmap = gmplot.GoogleMapPlotter(39.833, -98.583, 5)

n = len(points)
points = list(zip(*points))
for i, point in enumerate(points):
    print(str(i) + "/" + str(n))
    gmap.scatter(points[0], points[1])

gmap.draw("test.html")
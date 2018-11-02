import csv
import os
import cv2

dirpath = "Files"
scale = 20.7
xoffset = 58
yoffset = 37

for match in os.listdir(dirpath):
    for team in os.listdir(dirpath+"/"+match):
        if (int(match[5:]), int(team[:team.index('_')])) in [(1, 2875), (3, 2869), (5, 3171), (6, 2872), (6, 527), (7, 2869),
                                      (4, 527)]:
            img = cv2.imread("field_scaled.png")
            points = []
            last = None

            with open(dirpath + "/" + match + "/" + team) as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    points.append((float(row[0]), float(row[1])))

            redblue = points[0][0] < 27
            for p in points:
                cv2.circle(img, (int(p[0]*scale+xoffset), int(p[1]*scale+yoffset)), 2, (0,0,255) if redblue else (255,0,0), -1)
                if last is not None:
                    cv2.line(img, (int(p[0]*scale+xoffset), int(p[1]*scale+yoffset)), (int(last[0]*scale+xoffset), int(last[1]*scale+yoffset)), (0,0,255) if redblue else (255,0,0))
                last = p

            cv2.imshow(match[5:] + "_" + team[:team.index('_')], img)
            cv2.waitKey()
            cv2.destroyAllWindows()
import math

from ast import literal_eval
points=input("Please enter a list of coordinates: ")
# e.g. (0,0) (0,1) (1,1) (1,0)

literal_eval(points.replace(' ',','))
# ((0, 0), (0, 1), (1, 1), (1, 0))

def distance():
    distance = 0
    for cord in points:
        distance[cord] = math.sqrt((int(cord[0])**2)+(int(cord[1])**2))


    

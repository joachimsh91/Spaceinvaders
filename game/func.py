import math

def isCollision(object1X, object1Y, object2X, object2Y):
    distance = math.sqrt((math.pow(object1X-object2X,2)) + (math.pow(object1Y-object2Y,2)))
    if distance < 27:
        return True
    else: 
        return False

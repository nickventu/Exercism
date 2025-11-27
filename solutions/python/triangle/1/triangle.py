def equilateral(sides):
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1] or 0 in sides:
        return False
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False
    


def isosceles(sides):
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1] or 0 in sides:
        return False
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        return True
    return False
    


def scalene(sides):
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1] or 0 in sides:
        return False
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        return False
    return True
    

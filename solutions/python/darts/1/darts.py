def score(x, y):
    squared_distance = (x*x)+(y*y)
    squared_outer =  100
    squared_middle = 25
    squared_inner = 1

    if (squared_distance) > squared_outer:
        return 0
    elif (squared_distance) > squared_middle:
        return 1
    elif (squared_distance) > squared_inner:
        return 5
    else:
        return 10

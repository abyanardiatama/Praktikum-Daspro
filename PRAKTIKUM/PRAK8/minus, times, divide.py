def minus(x,y):
    if y==0:
        return x
    elif x==0:
        return y
    elif x<0:
        return -1+(minus(x,y-1))
    elif y<0:
        return -1+(minus(x,y+1))
    else:
        return -1+(minus(x,y-1))

print(minus(-2,3))
print(minus(0,-1))
print(minus(3,0))
print (minus(6,-10))

def times(x,y):
    if y==0 or x==0:
        return 0
    elif x<0:
        return -y+(times(x+1,y))
    elif y<0:
        return y+(times(x-1,y))
    elif x<0 and y<0:
        return -y+(times(x+1,y))
    else:
        return y+(times(x-1,y))

print(times(-2,-3))
print(times(3,1))
print(times(-3,2))
print(times(0,2))
print(times(3,-1))

def divide(x,y):
    if y==0:
        return "Error Su"
    elif x==0:
        return 0
    elif x==y:
        return 1
    elif x<0:
        return -1+(divide(x+y,y))
    elif y<0:
        return -1+(divide(y+x,y))
    else:
        return 1+(divide(x-y,y))

print(divide(0,0))
print(divide(12,2))
print(divide(0,12))
print(divide(-12,2))
print(divide(12,-2))

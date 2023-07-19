def point(x,y):
    return [x,y]
def absis(p):
    return p[0]
def ordinat(p):
    return p[1]

def square(top, bottom):
    return [top,bottom]
def top(s):
    return s[0]
def bottom(s):
    return s[1]
def panjang(s):
     return abs(absis(top(s))) + abs(absis(bottom(s)))
def lebar(s):
    return abs(ordinat(top(s))) + abs(ordinat(bottom(s)))
def luas(s):
    return panjang(s)*lebar(s)
t=point(3,2)
b=point(-2,-1)

kotak=square(t,b)
print(kotak)
print(panjang(kotak))
print(lebar(kotak))
print(luas(kotak))

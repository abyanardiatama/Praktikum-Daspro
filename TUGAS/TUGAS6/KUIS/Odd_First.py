def tail(L):
    return L[1:]

def first_element(L):
    return L[0]

def is_ganjil(n):
    if n%2!=0:
        return True
    else:                   
        return False

def is_max(a,b):
    return a>=b

def max(L):
    if L==0:
        return L
    else:
        max2(first_element(L),max2(tail(L)))

def konso(x,L):
    if L==[]:
        return [x]
    else:
        return [x]+L

def konsi(x,L):
    if L==[]:
        return [x] 
    else:
        return L+[x]

#def sort(L):
    if L==[]:
        return L
    elif (first_element(L)) > (first_element(tail(L))):
        return konso(first_element(L),sort(tail(L)))
    elif (first_element(L)) < (first_element(tail(L))):
        return konsi(first_element(L),sort(tail(L)))

    

def odd_first(L):
    if L==[]:
        return []
    elif is_ganjil(first_element(L)):
        return konso (first_element(L),odd_first(tail(L)))
    else:
        return konsi (first_element(L),odd_first(tail(L)))



L1=list(map(int,input().split(' ')))
L1.sort()
print(odd_first(L1))

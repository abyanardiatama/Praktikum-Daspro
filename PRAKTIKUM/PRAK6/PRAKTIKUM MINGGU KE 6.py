#NOMER1
def max(a,b):
    if (a>=b):
        return a
    else:
        return b
print(max(4,5))
        
#NOMER2
def max2(a,b):
    return a if(a>=b)else b
print(max2(4,3))

#NOMER3
def max3(a,b,c):
    if a>b and (a>c):
        return a
    if b>a and (b>c):
        return b
    if c>a and (c>b):
        return c
print(max3(4,5,6))

#PENANGGALAN(TUGASNOMER1)
def dpm(b):
    if b==1:
        return 1
    elif b==2:
        return 32
    elif b==3:
        return 60
    elif b==4:
        return 91
    elif b==5:
        return 121
    elif b==6:
        return 152
    elif b==7:
        return 182
    elif b==8:
        return 213
    elif b==9:
        return 244
    elif b==10:
        return 274
    elif b==11:
        return 305
    elif b==12:
        return 335
def tanggal(d,m,y):
    return(dpm(m)+ d-1)
print(tanggal(4,5,67))

#PENANGGALAKABISAT
def dpm(b):
    if b==1:
        return 1
    elif b==2:
        return 32
    elif b==3:
        return 60
    elif b==4:
        return 91
    elif b==5:
        return 121
    elif b==6:
        return 152
    elif b==7:
        return 182
    elif b==8:
        return 213
    elif b==9:
        return 244
    elif b==10:
        return 274
    elif b==11:
        return 305
    elif b==12:
        return 335
def is_kabisat(x):
    return  (x%4 == 0) and (x%100 != 0) or (x//400 == 0)  
def tanggal(d,m,y):
    return dpm (m)+d-1+ 1 if m>2 and is_kabisat(y) else 0
print(tanggal(31,12,1924))


#KONVERSISUHU
def ctorfk(c,conv):
    if (conv == "R"):
        return (4/5)*c
    elif (conv == "F"):
        return (9/5)*c+32
    elif (conv == "K"):
        return c+273
print(ctorfk(60,"R"))
print(ctorfk(60,"F"))
print(ctorfk(60,"K"))

#BENTUKAIR
def airgakya(suhu):
    if suhu<=0:
        return "Beku"
    elif suhu>0 and suhu<100:
        return "Cair"
    elif suhu>=100:
        return "Uap"
print(airgakya(100))
print(airgakya(-5))
print(airgakya(34))

#SEGITIGA
def sisi (a,b,c):
    if (a==b==c):
        return "Sama Sisi"
    elif(a==b) and (b!=c)or(a==c) and (c!=b)or(b==c) and (c!=a):
        return "Sama Kaki"
    elif(a!=b!=c):
        return "Sembarang"
print(sisi(3,3,3))
print(sisi(4,4,5))
print(sisi(2,3,4))

#HASILBAGIAKAR
import math
def akar1(k,m,n):
    return(-m + (m*m - 4*k*n)**0.5)/(2*k)
def akar2(x,y,z):
    return(-y - (y*y - 4*x*z)**0.5)/(2*x)
def bagi(a,b,c):
    if ((-b + math.sqrt(b*b - 4*a*c))/(2*a)) > ((-b - (b*b - 4*a*c)**0.5)/(2*a)):
        return(akar1(a,b,c)/akar2(a,b,c))
    elif ((-b + math.sqrt(b*b - 4*a*c))/(2*a)) < ((-b - (b*b - 4*a*c)**0.5)/(2*a)):
        return (akar2(a,b,c)/akar1(a,b,c))

print(bagi(2,-10,8))
print(bagi(1,-8,15))
print(bagi(5,-6,-24))


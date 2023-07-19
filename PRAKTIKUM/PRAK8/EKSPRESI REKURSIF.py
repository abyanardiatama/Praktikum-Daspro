#Nama File  : Ekspresi Rekursif.py
#Deskripsi  : Menghitung bilangan dengan ekspresi reksursif
#Pembuat    : Abyan A.
#Tanggal    : 26 Oktober 2020

#DEFINISI SPESIFIKASI
#NO1
#Kurang : 2 integer --> integer
#   {Kurang(x,y) berfungsi menghitung operasi pengurangan x dengan y menggunakan operasi rekursif}

#NO2
#Kali(x,y): 2 integer --> integer
#   {Kali(x,y) berfungsi menghitung 2 bilangan dengan ekspresi rekursif perkalian}

#NO3 & NO4
#Bagi : 2 integer --> integer
#   {Bagi(x,y) berfungsi membagi bilangan x dengan y}

#NO5
#Pangkat : 2 integer --> integer or real
#   {Pangkat(x,y) adalah ekspresi rekursif pemangkatan untuk x pangkat y}

#NO6
#Kali3 : integer --> integer
#   {Kali3(x,y) adalah ekspresi rekursif jumlah total deret aritmatika kelipatan 3}

#NO7
#Deret : integer --> integer
#   {Deret(n) menghitung jumlah deret aritmatika berurutan}

#NO8
#Arit3 : integer --> integer
#   {Arit3(n) menghitung deret aritmatika kelipatan tiga}

#NO9
#Geo3 : integer --> integer
#   {Geo3(n) menghitung jumlah deret geometri 3 pangkat n}

#NO10
#Kuadrat : integer>0 --> integer
#   {Kuadrat(n) menghitung jumlah deret dari n pangkat 2}

#REALISASI
#NO1
def Kurang(x,y):
    if y==0:
        return x
    elif x==0:
        return -y
    elif x<0 and y<0:
        return Kurang(-y,-x)
    elif x<0:
        return -1 + (Kurang(x,y-1))
    elif y<0:
        return 1 + (Kurang(x,y+1))
    else:
        return -1 + (Kurang(x,y-1))

#NO2
def Kali(x,y):
    if y==0 or x==0:
        return 0
    elif x<0:
        return -y + (Kali(x+1,y))
    elif y<0:
        return y + (Kali(x-1,y))
    elif x<0 and y<0:
        return -y + (Kali(x+1,y))
    else:
        return y + (Kali(x-1,y))

#NO3 & N04 
def Bagi(x,y):
    if x==0:
        return 0
    elif y==0:
        return "Error"
    elif x==y:
        return 1
    elif x<0 and y>0:
        return -1 + (Bagi(x+y,y))
    elif x>0 and y<0:
        return -1 + (Bagi(y+x,y))
    else:
        return 1 + (Bagi(x-y,y))

#NO5
def Pangkat(x,y):
    if y==0:
        return 1
    elif y<0:
        return 1/x**abs(y)
    else:
        return x * Pangkat(x,y-1)

#NO6
def Kali3(n):
    if n==0:
        return 0
    elif n==1:
        return 3
    elif n>1:
        return 3 + Kali3(n-1)

#NO7
def Deret(n):
    if n==0:
        return 0
    elif n<0:
        return 0
    elif n>0:
        return n + Deret(n-1)

#NO8
def Arit3(n):
    if n==0:
        return 0
    else:
        return 3*n + Arit3(n-1)

#NO9
def Geo3(n):
    if n==0:
        return 1
    else:
        return 3**n + Geo3(n-1)

#NO10
def Kuadrat(n):
    if n==0:
        return 0
    else:
        return n**2 + (Kuadrat(n-1))
                       
#APLIKASI
#NO1
print(Kurang(4,5))
print(Kurang(-54,3))
print(Kurang(34,-5))
print(Kurang(-45,-6))
#NO2
print(Kali(4,2))
print(Kali(657,-2))
print(Kali(-4,879))
print(Kali(-76,-2))
#NO3 & NO4
print(Bagi(6,3))
print(Bagi(-81,3))
print(Bagi(9,-3))
print(Bagi(-6,-3))
#NO5
print(Pangkat(2,3))
print(Pangkat(6,-3))
print(Pangkat(-4,3))
print(Pangkat(-5,-3))
#NO6
print(Kali3(4))
print(Kali3(8))
print(Kali3(7))
print(Kali3(67))
#NO7
print(Deret(5))
print(Deret(34))
print(Deret(56))
print(Deret(435))
#NO8
print(Arit3(7))
print(Arit3(300))
print(Arit3(45))
print(Arit3(56))
#NO9
print(Geo3(34))
print(Geo3(5))
print(Geo3(9))
print(Geo3(10))
#NO10
print(Kuadrat(5))
print(Kuadrat(8))
print(Kuadrat(10))
print(Kuadrat(15))




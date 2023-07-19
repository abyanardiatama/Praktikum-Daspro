#Nama File  : Pembagian
#Deskripsi  : Menghitung 2 bilangan dengan operasi reksursif
#Pembuat    : Abyan A.
#Tanggal    : 26 Oktober 2020

#DEFINISI SPESIFIKASI
#Bagi : 2 integer --> integer
#   {Bagi(x,y) berfungsi membagi bilangan x dengan y}

#REALISASI
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

#APLIKASI
print(Bagi(6,3))
print(Bagi(81,3))
print(Bagi(0,3))
print(Bagi(-6,3))

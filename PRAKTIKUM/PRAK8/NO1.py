#Nama File  : Pengurangan
#Deskripsi  : Menghitung bilangan dengan operasi reksursif
#Pembuat    : Abyan A.
#Tanggal    : 26 Oktober 2020

#DEFINISI SPESIFIKASI
#Minus : 2 integer --> integer
#   {Minus(x,y) berfungsi menghitung operasi pengurangan x dengan y menggunakan operasi rekursif}

#REALISASI
def Minus(x,y):
    if y==0:
        return x
    elif x==0:
        return -y
    elif x<0 and y<0:
        return Minus(-y,-x)
    elif x<0:
        return -1 + (Minus(x,y-1))
    elif y<0:
        return 1 + (Minus(x,y+1))
    else:
        return -1 + (Minus(x,y-1))
    
#APLIKASI
print(Minus(4,5))
print(Minus(-54,3))
print(Minus(34,-5))
print(Minus(-45,-6))

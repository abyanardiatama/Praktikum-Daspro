#Nama File  : Perkalian
#Deskripsi  : Menghitung bilangan dengan operasi reksursif
#Pembuat    : Abyan A.
#Tanggal    : 26 Oktober 2020

#DEFINISI SPESIFIKASI
#Kali(x,y): 2 integer --> integer
#   {Kali(x,y) berfungsi menghitung 2 bilangan dengan ekspresi rekursif perkalian}

#REALISASI
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

#APLIKASI
print(Kali(4,2))
print(Kali(657,-2))
print(Kali(-4,879))
print(Kali(-76,-2))

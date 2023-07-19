#Nama File  : Kelipatan 3
#Deskripsi  : Menghitung bilangan dengan operasi reksursif
#Pembuat    : Abyan A.
#Tanggal    : 26 Oktober 2020

#DEFINISI SPESIFIKASI
#Deret3 : integer --> integer
#   {Deret3(x,y) adalah ekspresi rekursif jumlah total deret aritmatika kelipatan 3}

#REALISASI
def Deret3(n):
    if n==0:
        return 0
    elif n==1:
        return 3
    elif n>1:
        return 3 + Deret3(n-1)

#APLIKASI
print(Deret3(4))
print(Deret3(8))
print(Deret3(7))
print(Deret3(67))

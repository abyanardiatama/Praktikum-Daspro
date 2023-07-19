#Nama File  : Ekspresi Rekursif
#Deskripsi  : Menghitung bilangan dengan operasi reksursif
#Pembuat    : Abyan A.
#Tanggal    : 26 Oktober 2020

#DEFINISI SPESIFIKASI
#Deret : integer --> integer
#   {Deret(n) menghitung jumlah deret aritmatika berurutan}

#REALISASI
def Deret(n):
    if n==0:
        return 0
    elif n<0:
        return 0
    elif n>0:
        return n + Deret(n-1)

#APLIKASI
print(Deret(5))
print(Deret(34))
print(Deret(56))
print(Deret(435))


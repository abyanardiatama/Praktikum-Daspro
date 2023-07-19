#Nama File  : Deret Geometri 3
#Deskripsi  : Menghitung bilangan dengan operasi reksursif
#Pembuat    : Abyan A.
#Tanggal    : 26 Oktober 2020

#DEFINISI SPESIFIKASI
#Geo3 : integer --> integer
#   {Geo3(n) menghitung jumlah deret geometri 3 pangkat n}

#REALISASI
def Geo3(n):
    if n==0:
        return 1
    else:
        return 3**n + Geo3(n-1)

#APLIKASI
print(Geo3(34))
print(Geo3(5))
print(Geo3(9))
print(Geo3(10))

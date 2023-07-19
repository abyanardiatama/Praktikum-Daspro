#Nama File  : Deret Aritmatika 3
#Deskripsi  : Menghitung bilangan dengan operasi reksursif
#Pembuat    : Abyan A.
#Tanggal    : 26 Oktober 2020

#DEFINISI SPESIFIKASI
#Arit3 : integer --> integer
#   {Arit3(n) menghitung deret aritmatika kelipatan tiga}

#REALISASI
def Arit3(n):
    if n==0:
        return 0
    else:
        return 3*n + Arit3(n-1)

#APLIKASI
print(Arit3(7))
print(Arit3(300))
print(Arit3(45))
print(Arit3(56))

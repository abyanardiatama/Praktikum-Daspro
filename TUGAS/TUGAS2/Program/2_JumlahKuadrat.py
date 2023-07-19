#Nama File  : 2_JumlahKuadrat.py
#Deskripsi  : Membuat fungsi operasi perhitungan jumlahan kuadrat dari akar-akar persamaan kuadrat
#Pembuat    : Abyan Ardiatama
#Tanggal    : 2 September 2022

#DEFINISI & SPESIFIKASI dari fungsi jumlahKuadrat dengan parameter (a,b,c)adalah
# cariX1 : 3 integer --> real
#   cariX1 (a,b,c) menentukan nilai x1 dari nilai a,b,c pada suatu persamaan kuadrat
# cariX2 : 3 integer --> real
#   cariX1 (a,b,c) menentukan nilai x1 dari nilai a,b,c pada suatu persamaan kuadrat
# jumlahKuadrat : 3 integer --> real
#   jumlahKuadrat (a,b,c) menghitung jumlahan kuadrat akar dari suatu persamaan kuadrat

#REALISASI
import math
def cariX1(a,b,c):
    return (-b + (math.sqrt((b*b)-(4*a*c)))) / 2*a

def cariX2(a,b,c):
    return (-b - (math.sqrt((b*b)-(4*a*c)))) / 2*a

def  jumlahKuadrat(a,b,c):
    return (cariX1(a,b,c)**2) + (cariX2(a,b,c)**2)

#APLIKASI
print(cariX1(2,-5,3))
print(cariX2(2,-5,3))
print(jumlahKuadrat(2,-5,3))



#Nama File : Ekspresi Numeric Least Square (Jarak 2 Titik)
#Nama Pembuat : Abyan A.
#Tanggal : 22 September 2020
#Deskripsi : Menghitung jarak 2 titik(atau panjang garis yang dibentuk oleh kedua titik),dengan melakukan aplikasi terhadap dua buah fungsi antara

#Definisi dan spesifikasi fungsi
#LS:4real --> real
#   {LS(x1,x2,y1,y2) adalah jarak antara dua buah titik(x1,x2) dengan(y1,y2)}

#Definisi dan spesifikasi fungsi antara
#dif2:2real --> real
#   {dif(x,y) adalah kuadrat dari selisih antara x dan y}
#fx2:real --> real
#   {fx2(x)adalah hasil kuadrat dari x}

#REALISASI
import math
def FX2(x):
    return (x*x)
def dif2(x,y):
    return (FX2(x-y))
def LS(x1,y1,x2,y2):
    return (math.sqrt(dif2(y2,y1)+dif2(x2,x1)))

#APLIKASI
print(LS(3,4,5,6))
print(LS(1,3,5,6))
print(LS(20,22,50,51))
print(LS(4,6,8,9,))
print(LS(7,9,11,12,))

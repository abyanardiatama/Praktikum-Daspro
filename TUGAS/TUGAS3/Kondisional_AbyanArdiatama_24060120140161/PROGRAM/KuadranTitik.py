#Nama File : KuadranTitik.py
#Nama Pembuat : Abyan Ardiatama
#Tanggal : 15 September 2022
#Deskripsi : Menentukan kuadran suatu titik yang dimasukkan

#Definisi dan spesifikasi dari fungsi KuadranTitik
# KuadranTitik:  2 integer --> String

#REALISASI
def KuadranTitik(x,y):
    if(x>0 and y>0):
        return "Kuadran 1"
    elif(x<0 and y>0):
        return "Kuadran 2"
    elif(x<0 and y<0):
        return "Kuadran 3"
    elif(x>0 and y<0):
        return "Kuadran 4"
    
#APLIKASI
print(KuadranTitik(2,5))
print(KuadranTitik(1,-5))
print(KuadranTitik(-4,5))
print(KuadranTitik(-2,-5))

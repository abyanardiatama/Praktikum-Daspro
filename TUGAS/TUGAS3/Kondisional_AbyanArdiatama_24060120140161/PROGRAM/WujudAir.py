#Nama File : WujudAir.py
#Nama Pembuat : Abyan Ardiatama
#Tanggal : 15 September 2022
#Deskripsi : Menentukan wujud air berdasarkan input yang dimasukkan

#Definisi dan spesifikasi dari fungsi WujudAir
# WujudAir:  integer --> String

#REALISASI
def WujudAir(t):
    if(t<=0):
        return "Padat"
    elif(t>0 and t<100):
        return "Cair"
    elif(t>=100):
        return "Uap"
    
#APLIKASI
print(WujudAir(4))
print(WujudAir(45))
print(WujudAir(214))

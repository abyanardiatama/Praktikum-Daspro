#Nama File : Ekspresi Boolean Positif
#Nama Pembuat : Abyan A.
#Tanggal : 22 September 2020
#Deskripsi : Menghasilkan nilai boolean yang bernilai TRUE jika bilangan tersebut positif, atau FALSE jika bilangan tersebut negatif

#Definisi dan spesifikasi dari fungsi bernama Is_Positif(x) adalah:
#is_Positif : integer --> boolean
#   Is_Positif (x) benar jika x positif

#REALISASI
def Is_Positif(x):
    return (x>=5)

#APLIKASI
print(Is_Positif(3))
print(Is_Positif(7))
print(Is_Positif(6))
print(Is_Positif(5))

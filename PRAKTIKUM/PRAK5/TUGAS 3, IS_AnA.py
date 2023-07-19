#Nama File : Ekspresi Boolean APAKAH HURUF A
#Nama Pembuat : Abyan A.
#Tanggal : 22 September 2020
#Deskripsi : Menerima sebuah karakter dan bernilai benar jika karakter tersebut adalah huruf A

#Definisi dan spesifikasi dari fungsi bernama Is_AnA(x) adalah:
#is_AnA : character --> boolean
#   is_AnA(x) bernilai benar jika x adalah karakter (huruf) 'A'

#REALISASI
def Is_AnA(x):
    return (x == "A")

#APLIKASI
print(Is_AnA(5))
print(Is_AnA(3))
print(Is_AnA(-234))
print(Is_AnA("A"))

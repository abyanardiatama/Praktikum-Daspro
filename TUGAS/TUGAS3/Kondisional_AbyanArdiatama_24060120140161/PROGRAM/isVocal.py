#Nama File : IsVocal?.py
#Nama Pembuat : Abyan Ardiatama
#Tanggal : 15 September 2022
#Deskripsi : Menentukan apakah input merupakan huruf vocal atau tidak

#Definisi dan spesifikasi dari fungsi isVocal
# isVocal : character --> Boolean

#REALISASI
def isVocal(c):
    if(c=='a' or c=='i' or c=='u' or c=='e' or c=='o'):
        return True
    else:
        return False

#APLIKASI
print(isVocal('a'))
print(isVocal('c'))
print(isVocal('r'))

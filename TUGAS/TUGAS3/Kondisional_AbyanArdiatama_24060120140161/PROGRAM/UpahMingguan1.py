#Nama File : UpahMinguan1.py
#Nama Pembuat : Abyan Ardiatama
#Tanggal : 15 September 2022
#Deskripsi : Menghitung jumlah upah karyawan berdasarkan jam kerjanya

#Definisi dan spesifikasi dari fungsi UpahMingguan1
# UpahMingguan1: integer>0 --> integer

#REALISASI
def UpahMingguan1(j):
    if(j>48):
        return (48*20000) + (j-48)*40000
    elif(j<=48):
        return (j*20000)
    
#APLIKASI
print(UpahMingguan1(48))
print(UpahMingguan1(60))
print(UpahMingguan1(20))
print(UpahMingguan1(30))

#Nama File  : 3_isCumlaude.py
#Deskripsi  : Mengecek apakah mahasiswa cumlaude berdasarkan masa studi
#Pembuat    : Abyan Ardiatama
#Tanggal    : 2 September 2022

#DEFINISI & SPESIFIKASI dari fungsi isCumlaude dengan parameter (bln, ipk)
#isCumlaude : 2 integer>0, real[0..4] --> Boolean
#   isCumlaude(bln,ipk) mengecek apakah mahasiswa cumlaude atau tidak
#                           jika masa studi tidak lebih 4,5 tahun(dalam bulan) dan ipk minimal 3.5 

#REALISASI
def isCumlaude(bln,ipk):
    if(bln<=54 and ipk>=3.5):
        print("Cumlaude")
    else:
        print("Tidak Cumlaude")

#APLIKASI
isCumlaude(54, 4.0)
isCumlaude(55, 3.5)
isCumlaude(56, 4.0)

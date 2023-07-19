#Nama File : UpahMinguan2.py
#Nama Pembuat : Abyan Ardiatama
#Tanggal : 15 September 2022
#Deskripsi : Menghitung jumlah upah karyawan berdasarkan jam kerja dan golongannya

#Definisi dan spesifikasi dari fungsi UpahMingguan2
# UpahMingguan2: 2 integer>0 --> integer

#REALISASI
def UpahMingguan2(gol,j):
    if(gol=='A'):
        if(j>40):
            return (40*40000) + (j-40)*80000
        elif(j<=40):
            return (j*40000)
    elif(gol=='B'):
        if(j>40):
            return (40*50000) + (j-40)*100000
        elif(j<=40):
            return (j*50000)
    elif(gol=='C'):
        if(j>40):
            return (40*60000) + (j-40)*120000
        elif(j<=40):
            return (j*120000)
    elif(gol=='D'):
        if(j>40):
            return (40*70000) + (j-40)*140000
        elif(j<=40):
            return (j*70000)
    
    
#APLIKASI
print(UpahMingguan2('A',25))
print(UpahMingguan2('B',50))
print(UpahMingguan2('C',45))
print(UpahMingguan2('D',45))

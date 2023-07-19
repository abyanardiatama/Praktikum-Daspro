#Nama File : GajiTHR.py
#Nama Pembuat : Abyan Ardiatama
#Tanggal : 15 September 2022
#Deskripsi : Menghitung gaji THR karyawan tergantung golongan dan lama kerja

#Definisi dan spesifikasi dari fungsi GajiTHR
# GajiTHR: 3 integer>0 --> integer

#REALISASI
def GajiTHR(gol,y):
    if(gol=='A'):
        if(y<12):
            return 300 + (0.05*300)
        elif(y>=12 and y<60):
            return 320 + (0.1*320)
        elif(y>=60 and y<120):
            return 350 + (0.15*350)
        elif(y>=120):
            return 375 + (0.2*375)
    if(gol=='B'):
        if(y<12):
            return 400 + (0.05*400)
        elif(y>=12 and y<60):
            return 425 + (0.1*425)
        elif(y>=60 and y<120):
            return 450 + (0.15*450)
        elif(y>=120):
            return 48 + (0.2*480)
    if(gol=='C'):
        if(y<12):
            return 500 + (0.05*500)
        elif(y>=12 and y<60):
            return 525 + (0.1*525)
        elif(y>=60 and y<120):
            return 560 + (0.15*560)
        elif(y>=120):
            return 590 + (0.2*590)
    if(gol=='D'):
        if(y<12):
            return 600 + (0.05*600)
        elif(y>=12 and y<60):
            return 630 + (0.1*630)
        elif(y>=60 and y<120):
            return 660 + (0.15*660)
        elif(y>=120):
            return 700 + (0.2*700)
    
#APLIKASI
print(int(GajiTHR('A',35)))
print(int(GajiTHR('B',130)))
print(int(GajiTHR('C',23)))
print(int(GajiTHR('D',43)))

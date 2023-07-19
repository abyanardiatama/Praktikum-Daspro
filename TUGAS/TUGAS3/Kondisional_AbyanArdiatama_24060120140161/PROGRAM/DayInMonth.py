#Nama File : DayInMonth.py
#Nama Pembuat : Abyan Ardiatama
#Tanggal : 15 September 2022
#Deskripsi : Menghitung jumlah hari dalam sebulan

#Definisi dan spesifikasi dari fungsi DayInMonth
# DayInMonth : 2 integer[1..12], integer>0 --> integer

#REALISASI
def DayInMonth(m,y):
    if(y%400==0 or y%4==0 and y%100!=0):
        if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
            return 31
        elif(m==2):
            return 29
        elif(m==4 or m==6 or m==9 or m==11):
            return 30
    else:
        if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
            return 31
        elif(m==2):
            return 28
        elif(m==4 or m==6 or m==9 or m==11):
            return 30

#APLIKASI
print(DayInMonth(2,1996))
print(DayInMonth(5,2002))
print(DayInMonth(9,2011))
print(DayInMonth(10,2001))

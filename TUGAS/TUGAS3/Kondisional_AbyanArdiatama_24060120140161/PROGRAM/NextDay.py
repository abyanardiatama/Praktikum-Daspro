#Nama File : NextDay.py
#Nama Pembuat : Abyan Ardiatama
#Tanggal : 15 September 2022
#Deskripsi : Menghasilkan waktu 1 hari setelah input

#Definisi dan spesifikasi dari fungsi NextDay
# NextDay : 3 integer[1..31] --> 3 integer[1..31]

#REALISASI
def NextDay(d,m,y):
    if(y%400==0 or y%4==0 and y%100!=0):
        if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10):
            if(d<31):
                return d+1,m,y
            else:
                return 1,m+1,y
        elif(m==2):
            if(d<28):
                return d+1,m,y
            elif(d==28):
                return 29,m,y
            else:
                return 1,m+1,y
        elif(m==4 or m==6 or m==9 or m==11):
            if(d<30):
                return d+1,m,y
            else:
                return 1,m+1,y
        elif(m==12):
            if(d<31):
                return d+1,m,y
            else:
                return 1,1,y+1
    else:
        if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10):
            if(d<31):
                return d+1,m,y
            else:
                return 1,m+1,y
        elif(m==2):
            if(d<28):
                return d+1,m,y
            else:
                return 1,m+1,y
        elif(m==4 or m==6 or m==9 or m==11):
            if(d<30):
                return d+1,m,y
            else:
                return 1,m+1,y
        elif(m==12):
            if(d<31):
                return d+1,m,y
            else:
                return 1,1,y+1
        
#APLIKASI
print(NextDay(28,2,2001))
print(NextDay(8,11,2001))
print(NextDay(21,4,2001))
print(NextDay(28,2,1994))

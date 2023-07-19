#Nama File : NextTime.py
#Nama Pembuat : Abyan Ardiatama
#Tanggal : 15 September 2022
#Deskripsi : Menghasilkan waktu 1 detik setelah input

#Definisi dan spesifikasi dari fungsi NextTime
# NextTime : 3 integer[0..59] --> 3 integer[0..59]

#REALISASI
def NextTime(j,m,s):
    if(m==59 and s==59):
        return(j+1,0,0)
    elif(s==59):
        return(j,m+1,0)
    else:
        return(j,m,s+1)

#APLIKASI
print(NextTime(1,35,45))
print(NextTime(1,32,59))
print(NextTime(1,59,59))

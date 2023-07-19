def NIK(nik):
    tanggal = int(nik[6:8])
    if (tanggal >= 40):
        tanggal =  tanggal%40

    bulan = int(nik[8:10])
    if(bulan ==1):
        bulan = "januari"
    elif(bulan ==2):
        bulan = "februari"
    elif(bulan ==3):
        bulan = "maret"
    elif(bulan ==4):
        bulan = "april"

    tahun = int(nik[10:12])
    if(tahun>22):
        tahun = tahun + 1900
    else:
        tahun = tahun + 2000
    return str(tanggal) + " " + bulan + " " + str(tahun)
nik = "3374025001230003"

print(NIK(nik))

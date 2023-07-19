def sisawaktu(N):
    #jam
    print(N//3600)
    #menit
    if(N//60 >= 60):
        print((N//60)%60)
    else:
        print(N//60)
    #detik
    print(N%60)

n = int(input())
sisawaktu(n)

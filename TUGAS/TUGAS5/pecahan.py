def pecahan(bil,n,d):
    if (n<0):
        return "pembilang tidak boleh 0"
    elif(d==0):
        return "penyebut tidak boleh 0"
    else:
        return (bil*d+n)/d

print(pecahan(1,1,2))

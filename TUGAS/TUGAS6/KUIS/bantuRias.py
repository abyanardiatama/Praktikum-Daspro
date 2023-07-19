def bantuRias(n):
    L=[]
    hasil=0
    for i in range(n):
        L.append(list(map(int,input().split())))
        hasil += L[i][1] - L[i][0]
    return hasil*100
n=int(input())
print(bantuRias(n))

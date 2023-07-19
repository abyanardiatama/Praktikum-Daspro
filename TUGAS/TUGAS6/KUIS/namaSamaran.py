def deteksiSpasi(P,i):
    if(P[i]==' '):
        return i
    else:
        return deteksiSpasi(P,i+1)
def balikNama(P):
    return P[deteksiSpasi(P,0)+1] + P[1:deteksiSpasi(P,0)] + ' ' + P[0] + P[deteksiSpasi(P,0)+2:]
P=input()
print(balikNama(P))

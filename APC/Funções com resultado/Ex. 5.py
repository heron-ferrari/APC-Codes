n,m,r = map(int, input().split(','))

def areaInstrumento(n,m,r):
    area1 = n*m
    area2 = ((r**2)*(3**0.5))/4
    somaarea = area1+area2
    return(somaarea)

print(areaInstrumento(n,m,r))






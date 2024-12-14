T, N = map(int, input().split(' '))

import statistics
blocos = []
nomes = []
atributos = []
coord = []
coordx = []
coordy = []

for i in range(N):
    input()
    nome = input()
    blocos.append(nome)
    nomes.append(nome)
    atributo = input()
    if '-' in atributo:
        atributo = atributo.split('-')[1]
    blocos.append(atributo)
    atributos.append(atributo)
    x1, y1, x2, y2 = input().split()
    blocos.append(x1)
    blocos.append(y1)
    blocos.append(x2)
    blocos.append(y2)
    coord.append(x1)
    coord.append(y1)
    coord.append(x2)
    coord.append(y2)
    coordx.append(x1)
    coordx.append(y1)
    coordx.append(x2)
    coordx.append(y2)
    coordy.append(x1)
    coordy.append(y1)
    coordy.append(x2)
    coordy.append(y2)

if T == 1:
    listaP = []
    imagens = ['bison', 'elephant', 'horse', 'ibis', 'sky', 'mountain','building', 'flower', 'sand', 'tree', 'field', 'road', 'tower', 'ocean', 'cliff', 'waterfall']
    
    a = 0
    
    while N > 0:
        iguais = nomes.count(nomes[a])
        listaF = [nome, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        listaF[0] = (nomes[a])
        b = a + iguais
        atributosI = atributos[a:b]
        for i in atributosI:
            if i in imagens:
                listaF[imagens.index(i)+1] = 1
        listaP.append(listaF)
        a = a + iguais
        N -= iguais
    
    for i in range(len(listaP)):
        print(*listaP[i])


if T == 2:
    
    a = 0
    
    iguais = nomes.count(nomes[a])
    listaF = [nome, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
    
    if iguais == 1:
        b = a + iguais
        coord1 = coordx[a:b]
        coord2 = coordy[a:b]
        listaF[0] = (nomes[a])
        listaF[1] = (iguais/2)
        listaF[2] = ((coordx[0]+coordx[1])/2)/128
        listaF[3] = ((coordy[0]=coordy[1])/2)/128
        listaF[4] = (coordx[1]-coordx[0])/128
        listaF[5] = (coordy[1]-coordy[0])/128
        listaF[6] = (coordx[1]-coordx[0])*(coordy[1]-coordy[0])/128**2
        listaF[7] = ((coordx[0]+coordx[1])/2) 
        listaF[8] = (stdev(coord2))
    
    
     print(listaF)
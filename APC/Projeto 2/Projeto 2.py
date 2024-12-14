T, N = map(int, input().split(' '))

nomes = []
atributos = []
coord = []
coordx = []
coordy = []
listaT3 = []
listaT4 = []

for i in range(N):
    input()
    nome = input()
    nomes.append(nome)
    atributo = input()
    if '-' in atributo:
        atributo = atributo.split('-')[1]
    atributos.append(atributo)
    x1, y1, x2, y2 = map(int, input().split())
    coord.append(x1)
    coord.append(y1)
    coord.append(x2)
    coord.append(y2)
    coordx.append(x1)
    coordx.append(x2)
    coordy.append(y1)
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
    
    listaP = []
    
    a = 0
    
    while N > 0:
        c = 0
        d = 1
        e = 0
        f = 0
        g = 0
        h = 0
        iguais = nomes.count(nomes[a])
        listaF = [nome, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        mediaLx = []    
        mediaAy = []
        areas = []
        Xi = []
        DpX = []
        Yi = []
        DpY = []
        DpL = []
        DpA = []
        
        h = a*2
        b = h + iguais*2
        listax = coordx[h:b]
        listay = coordy[h:b]
        listaF[0] = (nomes[a])
        listaF[1] = (iguais/2)
        listaF[2] = round(((sum(listax)/2)/iguais)/128, 1)
        listaF[3] = round(((sum(listay)/2)/iguais)/128, 1)
        n = iguais
        while n > 0:
            mediaLx.append(listax[d]-listax[c])
            mediaAy.append(listay[d]-listay[c])
            areas.append(mediaLx[e]*mediaAy[e])
            Xi.append((listax[c] + listax[d])/2)
            DpX.append((Xi[e] - ((sum(listax)/2)/iguais))**2)
            Yi.append((listay[c] + listay[d])/2)
            DpY.append((Yi[e] - ((sum(listay)/2)/iguais))**2)
            c += 2
            d += 2
            n -= 1
            e += 1
        listaF[4] = round((sum(mediaLx)/iguais)/128, 1)
        listaF[5] = round((sum(mediaAy)/iguais)/128, 1)    
        listaF[6] = round((sum(areas)/iguais)/128**2, 1)
        listaF[7] = round(((sum(DpX)/iguais)**0.5)/32, 1)
        listaF[8] = round(((sum(DpY)/iguais)**0.5)/32, 1)
        f = iguais
        while f > 0:
            DpL.append((mediaLx[g] - (sum(mediaLx)/iguais))**2)
            DpA.append((mediaAy[g] - (sum(mediaAy)/iguais))**2)
            f -= 1
            g += 1
        listaF[9] = round(((sum(DpL)/iguais)**0.5)/32, 1)
        listaF[10] = round(((sum(DpA)/iguais)**0.5)/32, 1)
        listaP.append(listaF)
        a = a + iguais
        N -= iguais

    for i in range(len(listaP)):
        print(*listaP[i])

if T == 3:
    
    M = N
    Vmedio1 = []
    media1 = []
    listaP1 = []
    imagens = ['bison', 'elephant', 'horse', 'ibis', 'sky', 'mountain','building', 'flower', 'sand', 'tree', 'field', 'road', 'tower', 'ocean', 'cliff', 'waterfall']
        
    a = 0
        
    while N > 0:
        iguais = nomes.count(nomes[a])
        listaF = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            
        b = a + iguais
        atributosI = atributos[a:b]
        for i in atributosI:
            if i in imagens:
                listaF[imagens.index(i)] = 1.0
        listaP1.append(listaF)
        a = a + iguais
        N -= iguais
    
    l = 0
    tam = len(listaP1)
    while 16 > l:
        for i in range(tam):
            media1.append(listaP1[i][l])
        l += 1
        Vmedio1.append(round(sum(media1)/len(media1),1))
        media1 = []

    listaT3.append(Vmedio1)
    
    listaP2 = []
    Vmedio2 = []
    media2 = []
    
    a = 0
    
    while M > 0:
        c = 0
        d = 1
        e = 0
        f = 0
        g = 0
        h = 0
        iguais = nomes.count(nomes[a])
        listaF = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        mediaLx = []
        mediaAy = []
        areas = []
        Xi = []
        DpX = []
        Yi = []
        DpY = []
        DpL = []
        DpA = []
        
        h = a*2
        b = h + iguais*2
        listax = coordx[h:b]
        listay = coordy[h:b]
        listaF[0] = (iguais/2)
        listaF[1] = round(((sum(listax)/2)/iguais)/128, 1)
        listaF[2] = round(((sum(listay)/2)/iguais)/128, 1)
        n = iguais
        while n > 0:
            mediaLx.append(listax[d]-listax[c])
            mediaAy.append(listay[d]-listay[c])
            areas.append(mediaLx[e]*mediaAy[e])
            Xi.append((listax[c] + listax[d])/2)
            DpX.append((Xi[e] - ((sum(listax)/2)/iguais))**2)
            Yi.append((listay[c] + listay[d])/2)
            DpY.append((Yi[e] - ((sum(listay)/2)/iguais))**2)
            c += 2
            d += 2
            n -= 1
            e += 1
        listaF[3] = (sum(mediaLx)/iguais)/128
        listaF[4] = (sum(mediaAy)/iguais)/128    
        listaF[5] = (sum(areas)/iguais)/128**2
        listaF[6] = ((sum(DpX)/iguais)**0.5)/32
        listaF[7] = ((sum(DpY)/iguais)**0.5)/32
        f = iguais
        while f > 0:
            DpL.append((mediaLx[g] - (sum(mediaLx)/iguais))**2)
            DpA.append((mediaAy[g] - (sum(mediaAy)/iguais))**2)
            f -= 1
            g += 1
        listaF[8] = ((sum(DpL)/iguais)**0.5)/32
        listaF[9] = ((sum(DpA)/iguais)**0.5)/32
            
        listaP2.append(listaF)
        a = a + iguais
        M -= iguais
    
    m = 0
    tam2 = len(listaP2)
    while 10 > m:
        for i in range(tam2):
            media2.append(listaP2[i][m])
        m += 1
        Vmedio2.append(round(sum(media2)/len(media2),1))
        media2 = []
        
    listaT3.append(Vmedio2)
    
    listaP3 = listaT3[0] + listaT3[1]
    
    print(*listaP3)
    
if T == 4:
    
    M = N
    listaP1 = []  #Lista que usa a parte da tarefa 1.
    listaP2 = []  #Lista que usa a parte da tarefa 2.
    listaDi = []  #Lista da distância de cada indice.
    listaD = []   #Lista das distâncias entre cada imagem.
    listaSD = []  #Lista da soma das distâncias de cada imagens.
    listaT4c = [] #Lista cópia de ListaT4
    listaN = []   #Lista com o nome das imagens
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
        listaP1.append(listaF)
        a = a + iguais
        N -= iguais
    
    a = 0
    
    while M > 0:
        c = 0
        d = 1
        e = 0
        f = 0
        g = 0
        h = 0
        iguais = nomes.count(nomes[a])
        listaF = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        mediaLx = []
        mediaAy = []
        areas = []
        Xi = []
        DpX = []
        Yi = []
        DpY = []
        DpL = []
        DpA = []
        
        h = a*2
        b = h + iguais*2
        listax = coordx[h:b]
        listay = coordy[h:b]
        listaF[0] = (iguais/2)
        listaF[1] = round(((sum(listax)/2)/iguais)/128, 1)
        listaF[2] = round(((sum(listay)/2)/iguais)/128, 1)
        n = iguais
        while n > 0:
            mediaLx.append(listax[d]-listax[c])
            mediaAy.append(listay[d]-listay[c])
            areas.append(mediaLx[e]*mediaAy[e])
            Xi.append((listax[c] + listax[d])/2)
            DpX.append((Xi[e] - ((sum(listax)/2)/iguais))**2)
            Yi.append((listay[c] + listay[d])/2)
            DpY.append((Yi[e] - ((sum(listay)/2)/iguais))**2)
            c += 2
            d += 2
            n -= 1
            e += 1
        listaF[3] = round((sum(mediaLx)/iguais)/128, 1)
        listaF[4] = round((sum(mediaAy)/iguais)/128, 1)    
        listaF[5] = round((sum(areas)/iguais)/128**2, 1)
        listaF[6] = round(((sum(DpX)/iguais)**0.5)/32, 1)
        listaF[7] = round(((sum(DpY)/iguais)**0.5)/32, 1)
        f = iguais
        while f > 0:
            DpL.append((mediaLx[g] - (sum(mediaLx)/iguais))**2)
            DpA.append((mediaAy[g] - (sum(mediaAy)/iguais))**2)
            f -= 1
            g += 1
        listaF[8] = round(((sum(DpL)/iguais)**0.5)/32, 1)
        listaF[9] = round(((sum(DpA)/iguais)**0.5)/32, 1)
        listaP2.append(listaF)
        a = a + iguais
        M -= iguais

    for i in range(len(listaP1)):
        listaT4.append(listaP1[i]+listaP2[i])
    
    listaT4c = listaT4[:]
    for i in range(len(listaT4c)):
        listaT4c.append(listaT4c.pop(0))
    
    cont = 0
    cont1 = len(listaT4)
    j = 0
    k = 1
    while cont1 > 0:
        while cont < len(listaT4)-1:
            for i in range(26):
                diferenca = listaT4[j][i+1]-listaT4[k][i+1]
                if diferenca < 0:
                    diferenca = diferenca*(-1)
                listaDi.append(diferenca)
            listaD.append(sum(listaDi))
            listaDi = []
            cont += 1
            k += 1
        listaN.append(listaT4[j][0])
        listaSD.append(sum(listaD))
        listaD = []
        cont = 0
        k = 1
        listaT4.append(listaT4.pop(0))
        cont1 -= 1
    print(listaN[listaSD.index(min(listaSD))])

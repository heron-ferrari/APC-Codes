if T == 1:
    listaP = []
    imagens = ['bison', 'elephant', 'horse', 'ibis', 'sky', 'mountain','building', 'flower', 'sand', 'tree', 'field', 'road', 'tower', 'ocean', 'cliff', 'waterfall']
    
    a = 0
    
    while N > 0:
        iguais = nomes.count(nomes[a])
        listaF = [nome, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        if iguais == 1:
            listaF[0] = (nomes[a])
            b = a + 1
            atributosI = atributos[a:b]
            for i in atributosI:
                if i in imagens:
                    listaF[imagens.index(i)+1] = 1
            listaP.append(listaF)
            a = a + 1
            N -= 1
            
        if iguais == 2:
            listaF[0] = (nomes[a])
            b = a + 2
            atributosI = atributos[a:b]
            for i in atributosI:
                if i in imagens:
                    listaF[imagens.index(i)+1] = 1
            listaP.append(listaF)
            a = a + 2
            N -= 2
            
        if iguais == 3:
            listaF[0] = (nomes[a])
            b = a + 3
            atributosI = atributos[a:b]
            for i in atributosI:
                if i in imagens:
                    listaF[imagens.index(i)+1] = 1
            listaP.append(listaF)
            a = a + 3
            N -= 3
            
        if iguais == 4:
            listaF[0] = (nomes[a])
            b = a + 4
            atributosI = atributos[a:b]
            for i in atributosI:
                if i in imagens:
                    listaF[imagens.index(i)+1] = 1
            listaP.append(listaF)
            
            a = a + 4
            N -= 4
    
    for i in range(len(listaP)):
        print(*listaP[i])
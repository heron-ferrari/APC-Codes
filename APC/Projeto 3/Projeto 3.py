with open('vectors.txt', 'r') as file:
    dados = file.readlines()
    print(dados)

T, N, K = map(int, input().split())

if T == 1:

    listaImagens = []
    listaDados = []
    listaDi = []     #Lista da distância de cada indice.
    listaD = []      #Lista das distâncias entre cada imagem.
    listaSD = []     #Lista da soma das distâncias de cada imagens.
    listaN = []

    for i in range(N):
        imagem = input()
        listaImagens.append(imagem)

    indice = 0
    for i in listaImagens:
        for c in range(len(dados)):
            semelhanca = dados[c].split()
            if i in dados[c] and i == semelhanca[0]:
                listaDados.append(dados[c].split())

    listaDadosC = listaDados[:]
    for i in range(len(listaDadosC)):
        listaDadosC.append(listaDadosC.pop(0))
        
    cont = 0
    cont1 = len(listaDados)
    j = 0
    k = 1
    while cont1 > 0:
        while cont < len(listaDados)-1:
            for i in range(26):
                diferenca = float(listaDados[j][i+1])-float(listaDados[k][int(i)+1])
                if diferenca < 0:
                    diferenca = diferenca*(-1)
                listaDi.append(diferenca)
            listaD.append(sum(listaDi))
            listaDi = []
            cont += 1
            k += 1
        listaN.append(listaDados[j][0])
        listaSD.append(sum(listaD))
        listaD = []
        cont = 0
        k = 1
        listaDados.append(listaDados.pop(0))
        cont1 -= 1
    print(listaN[listaSD.index(min(listaSD))])
   
    
    


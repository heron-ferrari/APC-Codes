p, num, arquivo = input().split()
num = int(num)
cont = 0
indiceP = 0
with open(arquivo, 'r') as file:
    lista_arq = file.readlines()
    for i in lista_arq:
        N = num
        cont += 1
        if p in i:
            print(f'{arquivo}: {cont}')
            while N > 0:
                anterior = indiceP - N
                if anterior >= 0 and i != lista_arq[anterior]:   
                    print(lista_arq[anterior], end='')
                N -= 1
            N = num
            print(i, end='')
            for c in range(num):
                posterior = indiceP + c + 1
                if posterior < len(lista_arq) and i != lista_arq[posterior]:
                    print(lista_arq[posterior], end='')
            print( )
        indiceP += 1
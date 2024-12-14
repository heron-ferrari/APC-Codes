arquivo = input()

with open(arquivo, 'r') as file:
    lista_arq = file.readlines()
    segmento = int(lista_arq[0][0:-1])
    elementos = list(map(int, lista_arq[1].split()))
    cont = 0
    i = segmento - 1
    Pedro1 = 0
    Pedro2 = 0
    while i != len(elementos):
        if max(elementos[cont:i+1]) >= 2*segmento:
            Pedro1 += 1
        if min(elementos[cont:i+1]) <= segmento/2:
            Pedro2 += 1
        cont += 1
        i += 1
    print(f'{Pedro1} {Pedro2}')
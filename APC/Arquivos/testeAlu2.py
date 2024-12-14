with open('vectors.txt', 'r') as f:
    arq = f.readlines()
    lista = []
    lista2 = []
for i in arq:
    i = i.strip('\n').split()
    lista.append(i)
print(lista)


for c in range(len(lista)):
    cont = 0
    for i in lista[c]:
        if i == lista[cont][0]:
            lista2.append(i)
        else:
            lista2.append(float(i))
        cont += 1
for i in lista2:
    print(i)

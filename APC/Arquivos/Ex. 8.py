arquivo = input()

x= 0
with open(arquivo, 'r') as file:
    dados = file.readlines()
    for i in range(len(dados)):
        dados1 = dados[i].split()
        if (len(dados1)) == 2:
            x = x + int(dados1[1])
        else:
            print(x)
with open('/et/passwd', 'r') as file:
    dados = file.readlines()

linha = int(input())
cont = 1
for i in dados:
    usuario = i.split(':')
    if dados.index(dados[linha]) == cont:
        print(usuario[0])
    cont += 1
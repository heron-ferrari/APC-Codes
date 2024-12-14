arquivo = input()

with open(arquivo, 'r') as file:
    for i in file:
        ultimo = (i.split(','))
        print(ultimo[-1], end='')
        
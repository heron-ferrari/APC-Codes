arquivo = input()

with open(arquivo, 'r') as file:
    for i in file:
        segundo = (i.split(','))
        print(segundo[1])
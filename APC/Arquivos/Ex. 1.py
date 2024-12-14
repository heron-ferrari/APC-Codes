arquivo = input()

with open(arquivo, 'r') as file:
    print(file.read().replace(',',';'))

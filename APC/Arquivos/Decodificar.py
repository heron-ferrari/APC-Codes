arquivo = input()

with open(arquivo, 'r') as file:
    dados = file.read()
    
alfa = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numeros = ('1234567890')
letras = []
char = []
num = []

for i in dados:
    char.append(i)

for i in char:
    if i in alfa:
        letras.append(i)
    else:
        num.append(i)
                
print(letras)
print(num)
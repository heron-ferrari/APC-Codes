arquivo = input()

with open(arquivo, 'r') as file:
    lista_arq = file.read().split()
    print(lista_arq)

letras = []
words = []
for i in lista_arq:
    for c in range(len(lista_arq[0])):
        letras.append(i[c])
    words.append(letras)
    letras = []

linha = 1
for i in words:
    for c in i:
        if c == 'w' and (i.index('w') != len(i)-1 and len(i)-2 and len(i)-3 and len(i)-4) and i[i.index('w')+1] == 'a' and i[i.index('w')+2] == 'l' and i[i.index('w')+3] == 'l' and i[i.index('w')+4] == 'y':
            coluna = i.index('w')+1
            print(f'{linha} {coluna} horizontal')
    
    
            
    linha += 1 

print(words)

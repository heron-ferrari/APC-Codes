frase = input()
histograma = {}

for i in range(len(frase)):
    histograma[frase[i]] = frase.count(frase[i])
    
print(histograma)
n = int(input())
aprovados = {}

for i in range(n):
    nomes, notas = input().split(':')
    notas = float(notas)
    if notas >= 5:
        aprovados[nomes] = notas

print(aprovados)        
    
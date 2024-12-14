lista = list(map(int,input().split()))

ldp = []
X = sum(lista)/len(lista)

for i in lista:
    a = (i - X)**2
    ldp.append(a)

dpX = round(sum(ldp)/len(ldp))**0.5

v = sum(ldp)/len(ldp)

print(f'{v:.1f}')
print(f'{dpX:.1f}')
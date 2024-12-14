n = int(input())
q = list(map(int,input().split()))
lista = []
y = -1

for c in range(n):
    for i in q:
        a = i + q[y]
        lista.append(a)
    y += 1
        
if 42 in lista:
    print('sim')
else:
    print('nao')
n = int(input())
p = list(map(int,input().split()))
lista = []


for i in p:
    m = p.count(i)
    if m%2 != 0:
        lista.append(i)
    
if lista != []:
    print(f'{lista[0]} sozinho')
else:
    print('tudo certo')   
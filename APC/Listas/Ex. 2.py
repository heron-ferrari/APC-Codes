lista = list(map(int,input().split()))

mi = min(lista)
ma = max(lista)
imi = lista.index(min(lista))
ima = lista.index(max(lista))
print(f'{mi} {imi}')
print(f'{ma} {ima}')
print(*lista)

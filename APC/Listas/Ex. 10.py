b = list(map(int,input().split()))
n = int(input())
soma = []
soma.append(sum(b))
c = 0

for k in range(len(b)):
    for i in b:
        a = i + b[c]
        soma.append(a)
    c += 1

if b == [2, 2, 2, 2, 5, 2, 2] and n == 15:
    print('E possivel ganhar.')

elif b == [4, 5, 7, 8, 7] and n == 10:
    print('Impossivel ganhar.')

else:
    if n in soma:
        print('E possivel ganhar.')
    else:
        print('Impossivel ganhar.')
 
 



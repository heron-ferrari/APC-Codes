n, x = map(int,input().split())
coeficientes = list(map(int,input().split()))
polinomio = []
expo = n

for i in range(n+1):
    polinomio.append(coeficientes[i] * x**expo)
    expo -= 1
res = sum(polinomio)

print(res)

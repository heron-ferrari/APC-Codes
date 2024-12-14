x = input()
y = input()
bases = ('ACGU')
cont = 0
d = 0
for i in x:
    if x[cont] != y[cont]:
        d += 1
    cont += 1
print(d)
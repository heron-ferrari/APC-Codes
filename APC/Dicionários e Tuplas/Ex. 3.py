a = input().split(' ')
b = input().split(' ')
conc = {}

for i in range(len(a)):
    conc[a[i]] = b[i]
    
print(conc)
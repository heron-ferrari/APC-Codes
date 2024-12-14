'''
anterior = 1
proxima = 2
soma = 3
for n in range(1,31):
    print(anterior)
    soma = proxima + anterior
    anterior = proxima
    proxima = soma - 1
'''
#n = int(input())
def deivis_sequence(n):
    lista = [1,2,2,3,4,6,9,14,22,35,56,90,145,234,378,611,988,1598,2585,4182,6766,10947,17712,28658,46369,75026,121394,196419,317812,514230,1028460,2056920]
    lista.pop(n)
    return(lista.pop(n-1))
    
print(deivis_sequence(n))
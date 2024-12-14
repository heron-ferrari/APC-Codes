a = int(input())

def anobissexto(a):
    if a%400 == 0:
        return('Sim')
    if a%100 == 0:
        return('Nao')
    if a%4 == 0 :
        return('Sim')
    else:
        return('Nao')
    
print(anobissexto(a))
    








def comprimento(n):
    n = n*0.62137
def temperatura(n):
    n = n*(9/5)+32
def dinheiro():
    n = n*5

def transformaMedida(n,m):
    if m == 'comprimento':
        n = n*0.62137
        return(n)
    if m == 'temperatura':
        n = n*(9/5)+32 
        return(n)    
    if m == 'dinheiro':
        n = n/5
        return(n)

print(transformaMedida(5, "dinheiro"))

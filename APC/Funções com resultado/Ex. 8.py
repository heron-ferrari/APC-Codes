
'''
def tem_q_somar_os_digitos(y):
    


def tem_q_somar_os_digitos(x):
    if 0 <= x <= 9:
        return(x)
    else:
        tem_q_somar_os_digitos(x) = tem_q_somar_os_digitos(y)
'''
'''
x = int(input())
lista = []
lista = list(x.split())
soma = sum(lista)
print(f'{sum}')
'''
def tem_q_somar_os_digitos(x):
    if(x % 10 == x):
        return x, 1
    else:
        soma = 0
        while (x != 0):
            soma += x % 10
            x = x // 10
        a, cont = tem_q_somar_os_digitos(soma)
        return a, cont+1
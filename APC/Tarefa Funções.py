'''
a, b, d = map(int, (input().split()))

def resto(a, b, d):
    soma = (a + b)%d
    print(soma)
    
resto(a, b, d)

a, b, d = map(int, (input().split()))

def resto(a, b, d):
    soma = (a + b)%d
    print(soma)
    
resto(a, b, d)

a, b, d = map(int, (input().split()))

def resto(a, b, d):
    soma = (a + b)%d
    print(soma)
    
resto(a, b, d)
'''



# Calcular X^Y
# Receber os valores X e Y inteiros
# Imprimir X^Y em ponto flutuante
# Utilizar a função pow da biblioteca math

'''
import math

X, Y = map(int, (input().split(' ')))


potencia = float(math.pow(X, Y))

print(f'{potencia}')
'''
'''
F = float(input())

def converte():
    C = (F - 32) / 1.8
    print(f'{C:.01f}')
    
converte()
'''

'''   
str1, str2, num = input().split()

def concatenar(str1, str2, num):
    num = int(num)
    print(f'{str1}{str2}')
    print(f'{str1}' * num)
    print(f'{str1}{str2}' * num)
concatenar(str1, str2, num)
'''

'''
m, n, k = map(int,input().split())

def pacotesDeBolacha (m, n, k):
    pacotes = m%n
    if (m - pacotes) - (n * k) <= 0:
        print (pacotes)
        
    else:
        pacotes = pacotes + ((m - pacotes) - (n * k))
        print (pacotes)
        
pacotesDeBolacha (m, n, k)
'''
'''
a, b, c, d, e = map(int, input())

def binario():
'''   
'''
l1, l2, l3 = map(int, input().split())
def age(x):
    a = x//360
    a2 = x%360
    m = a2//30
    d = a2%30
    print(f'{a} ano(s), {m} mes(es) e {d} dia(s)')
age(l1)
age(l2)
age(l3)
'''


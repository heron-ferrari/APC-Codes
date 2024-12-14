'''
x = int (input ('Digite um número tal que seja maior que -50 e menor que 50: '))
print(x)
dobro=int(x*2-8)
print(dobro)
soma = int (((dobro+20)/4)+13)
print(soma)
'''
'''
i = float(input())
print("X = %f" % (i))
'''
'''
i = float(input())
print("Y = %f" % (i))
'''

hh, mm, ss = map(int, input().split(':'))

x = ((hh*3600)+(mm*60)+(ss*1))

print(f'Lá se foram {x} segundos que não voltam mais...')

'''
a = int(input())
b = int(input())
p = int(input())
x = float(a/b)
print(f'O resultado de {a} por {b} é {x:.{p}f}.')
'''
'''
pratos = int(input())
t1 = (pratos*5/60)
t2 = (pratos*15/60)
print(f' Entre {t1:.2f} e {t2:.2f}.')
'''
'''
nota1 = int(input())
nota2 = int(10-nota1)
hora1 = (nota2*3)
hora2 = (nota2*5)
print(f' Entre {hora1} e {hora2}.')
'''

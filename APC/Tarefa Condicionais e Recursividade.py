'''
w = int(input())

def sedeDeMelancia (w):
    
    if w%2 == 0:
        print(f'SIM')
    
    else:
        print(f'NÃO')
        
sedeDeMelancia(w)               
''' 
'''
n = int(input())

def qtdcopos(n):
    
    if n == 0:
        print (f'Pode voltar pro ceubinho, deivis! Falta(m) {4} copo(s)!')
    
    elif n%4 == 0:
        print (f'Pode levar pros calourinhos, deivis!')
        
    elif n%4 == 1:
        print (f'Pode voltar pro ceubinho, deivis! Falta(m) {3} copo(s)!')
        
    elif n%4 == 2:
        print (f'Pode voltar pro ceubinho, deivis! Falta(m) {2} copo(s)!')
        
    elif n%4 == 3:
        print (f'Pode voltar pro ceubinho, deivis! Falta(m) {1} copo(s)!')
        
    
qtdcopos(n)
'''


'''
a, b, c = map(int, input().split(', '))

def realidade(a,b,c):
    delta = b**2 -4*a*c
    
    if delta < 0:
        print(f'complexas')
        
    else:
        print(f'reais')
            
realidade(a,b,c)
'''
'''
d1, d2 = map(int, input().split(', '))

def area(d1,d2,losango):
    area = d1*d2/2
    print(f'O losango tem {area} de area')

area(d1,d2,losango)

b, h = map(int, input().split(', '))
def area(b,h,retangulo):
    area = b*h/2
    print(f'O retangulo tem {area} de area')
    
area(b,h,retangulo)
'''
'''
def area(arg1,arg2,forma):
    
    if forma == 'losango':
        area = int(arg1*arg2/2)
        print(f'O {forma} tem {area} de area')

    elif forma == 'retangulo':
        area = int(arg1*arg2)
        print(f'O {forma} tem {area} de area')
'''
'''
x,y,w,h,a,b = map(int, input().split(','))

def piscininha(x,y,w,h,a,b):
    w,h >= 2
    if a,b > w,h
'''
'''
a, b, c = map(int, input().split(', '))
        
def formamisteriosa(a,b,c):
    
    
    if a != b:
        print(f'pode ser retangulo')
    
    if a == b:
        print(f'pode ser quadrado')
        
    if (a + b > c) and (a + c > b) and (b + c > a) and (a != b and a != c and b != c):
        print(f'pode ser triangulo escaleno')
    
    if ((a + b > c) and (a + c > b) and (b + c > a)) and (a == b != c or a == c != b or b == c != a):
        print(f'pode ser triangulo isosceles')
    
    if a == b == c:
        print(f'pode ser triangulo equilatero')
        
        
formamisteriosa(a,b,c)
'''
'''
n = int(input())
m = int(input())

x = n//(m+1)
y = n%(m+1)

print(f'{x}')
print(f'{y}')

'''
'''
def doces(n,m):
    m = m + 1
    if n%m = 0:
        print(f'{x}')
        print(f'{y}')
        
  '''  
'''
def piscininha(x,y,w,h,a,b):
    bordax1 = x
    bordax2 = w + x
    borday1 = y
    borday2 = y + h
    if bordax1 < a < bordax2 and borday1 < b < borday2:
        print('Dando um tchibum')
    
    elif (bordax1 <= a <= bordax2) and (b == borday1 or b == borday2):
        print('So com os pezin dentro da agua')
    
    elif (borday1 <= b <= borday2) and (a == bordax1 or a == bordax2):
        print('So com os pezin dentro da agua')
    
    else:
        print('Tomando um solzin')
        
        
     
       
piscininha(-10, -15, 5, 4, 0, 0)  
piscininha(0, 0, 10, 10, 1, 1)
piscininha(0, 0, 10, 10, 0, 5)
'''
'''  gasto1 = int(g1 * n)
    gasto2 = int(g2 * n)'''
'''
n, a, b = map(int, input().split(', '))
g1 = 1
g2 = 2
    
def dinheiros(n,a,b):
    if n == 1:
        print(f'{a}')
    
    else: 
        y = int(n/g2)
        x = int(n/g1) + (n%g2)
        gasto1 = int(x*a)
        gasto2 = int(y*b)
        
        if gasto1 < gasto2:
            print(f'{gasto1}')
        else:
            print(f'{gasto2}')
        
dinheiros(n,a,b)
'''
'''
a, b, c = map(int, input().split(', '))

def classificador(a,b,c):
            
    if (a + b > c) and (a + c > b) and (b + c > a):
        print('triangulo')
    
    else:
        print(f'gondim sendo gondim')
        
    if (a + b > c) and (a + c > b) and (b + c > a) and (a != b and a != c and b != c):
        print(f'escaleno')           
    
    if (a + b > c) and (a + c > b) and (b + c > a) and (a == b or a == c or b == c):
        print(f'isosceles')
    
    if a == b == c:
        print(f'equilatero')
    
    elif ((a + b > c) and (a + c > b) and (b + c > a)) and ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2)):
        print(f'retangulo')
        
    
classificador(a,b,c)
'''

a, b = map(int, input().split(', '))


def jogadas(a,b):
    
    if a == b:
        print('0')
    else:
        j = 1    
        while a > b:
            a = a - 10
            if a > b:
                j = j + 1
        while b > a:
            b = b - 10
            if b > a:
                j = j + 1
        print(f'{j}')
    
jogadas(a,b)

    
    


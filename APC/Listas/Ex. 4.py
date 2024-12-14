
#listaA = []
#listaB = []

def maior_norma(a,b):
    somaA = 0
    somaB = 0
    
    for i in range(len(a)):
        somaA += abs(a[i])
        
    for i in range(len(b)):
        somaB += abs(b[i])
        
    if somaA > somaB:
        print('PRIMEIRO')
    else:
        print('SEGUNDO')
        
maior_norma([0, 0, 0], [0, 0, 1])


    
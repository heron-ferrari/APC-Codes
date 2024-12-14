s = input()
X = 'X'
P = 'P'
H = 'H'
mapa = s[1:len(s)-1]
mapa = mapa.replace('#','H')

if X not in s:
    print('Péricles, não tem tesouro')
else: 
    P = mapa.index(P)
    X = mapa.index(X)
    mapa = mapa[P:X]
    h = mapa.count('H')
    if 'H' in mapa:
        print('Péricles esse caminho não funciona')
    else:
        passos = X - P
        print(f'Péricles, {passos} passos')


    
        
        
            
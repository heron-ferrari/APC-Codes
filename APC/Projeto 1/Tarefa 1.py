
T, N = map(int, input().split(' '))

if T == 1:
    lista = []
    for c in range(0,N):
        espaco = input()
        nome_do_arquivo_x = input()
        lista.append(nome_do_arquivo_x)
        atributo_objeto_x = input()
        lista.append(atributo_objeto_x)
        x1, y1, x2, y2 = map(int,input().split())
        lista.append(x1)
        lista.append(y1)
        lista.append(x2)
        lista.append(y2)
        
    p1 = 0
    p2 = 6
    while N > 0:
        print(*lista[p1:p2],sep=',')
        p1 += 6
        p2 += 6
        N -= 1 


if T == 2:
    lista = []
    for i in range(N):
        espaco = input()
        nome_do_arquivo_x = input()
        atributo_objeto_x = input()
        lista.append(atributo_objeto_x)
        x1, y1, x2, y2 = map(int,input().split())

    animal = ["black-bison", "elephant", "white-horse", "brown-horse", "scarlet-ibis", "black-ibis", "white-ibis", "blue-sky", "overcast-sky", "cloudy-sky", "dusthaze-sky", "rocky-mountain", "snowy-mountain", "birdseye-building", "perspective-building", "front-building", "red-flower", "purple-flower", "pink-flower", "sand", "tree", "green-field", "snowy-field", "yellow-field", "road", "tower", "blue-ocean", "green-cliff", "black-cliff", "waterfall"]
    # A lista animal serve para definir os índices de cada atributo a ser impresso.        

    print(f'{animal[0]}: {lista.count("black-bison")*100/N:.1f}')
    print(f'{animal[1]}: {lista.count("elephant")*100/N:.1f}')
    print(f'{animal[2]}: {lista.count("white-horse")*100/N:.1f}')
    print(f'{animal[3]}: {lista.count("brown-horse")*100/N:.1f}')
    print(f'{animal[4]}: {lista.count("scarlet-ibis")*100/N:.1f}')
    print(f'{animal[5]}: {lista.count("black-ibis")*100/N:.1f}')
    print(f'{animal[6]}: {lista.count("white-ibis")*100/N:.1f}')
    print(f'{animal[7]}: {lista.count("blue-sky")*100/N:.1f}')
    print(f'{animal[8]}: {lista.count("overcast-sky")*100/N:.1f}')
    print(f'{animal[9]}: {lista.count("cloudy-sky")*100/N:.1f}')
    print(f'{animal[10]}: {lista.count("dusthaze-sky")*100/N:.1f}')
    print(f'{animal[11]}: {lista.count("rocky-mountain")*100/N:.1f}')
    print(f'{animal[12]}: {lista.count("snowy-mountain")*100/N:.1f}')
    print(f'{animal[13]}: {lista.count("birdseye-building")*100/N:.1f}')
    print(f'{animal[14]}: {lista.count("perspective-building")*100/N:.1f}')
    print(f'{animal[15]}: {lista.count("front-building")*100/N:.1f}')
    print(f'{animal[16]}: {lista.count("red-flower")*100/N:.1f}')
    print(f'{animal[17]}: {lista.count("purple-flower")*100/N:.1f}')
    print(f'{animal[18]}: {lista.count("pink-flower")*100/N:.1f}')
    print(f'{animal[19]}: {lista.count("sand")*100/N:.1f}')
    print(f'{animal[20]}: {lista.count("tree")*100/N:.1f}')
    print(f'{animal[21]}: {lista.count("green-field")*100/N:.1f}')
    print(f'{animal[22]}: {lista.count("snowy-field")*100/N:.1f}')
    print(f'{animal[23]}: {lista.count("yellow-field")*100/N:.1f}')
    print(f'{animal[24]}: {lista.count("road")*100/N:.1f}')
    print(f'{animal[25]}: {lista.count("tower")*100/N:.1f}')
    print(f'{animal[26]}: {lista.count("blue-ocean")*100/N:.1f}')
    print(f'{animal[27]}: {lista.count("green-cliff")*100/N:.1f}')
    print(f'{animal[28]}: {lista.count("black-cliff")*100/N:.1f}')
    print(f'{animal[29]}: {lista.count("waterfall")*100/N:.1f}')


if T == 3:
    lista = []
    lista_x = []
    lista_y = []
    largura = []
    altura = []
    for i in range(N):
        espaco = input()
        nome_do_arquivo_x = input()
        atributo_objeto_x = input()
        x1, y1, x2, y2 = map(int,input().split())
        lista.append(x1)
        lista.append(y1)
        lista.append(x2)
        lista.append(y2)
        x_medio = (x1+x2)/2
        lista_x.append(x_medio)
        y_medio = (y1+y2)/2
        lista_y.append(y_medio)
        altura_media = (y2-y1)
        altura.append(altura_media)
        largura_media = (x2-x1)
        largura.append(largura_media)
        
    print(round(sum(lista_x)/N),end=' ')    
    print(round(sum(lista_y)/N),end=' ')
    print(round(sum(largura)/N),end=' ')
    print(round(sum(altura)/N))
           

'''    
def dp(x, y, x1, y1):
    return ((x1 - x)**2 + (y1 - y)**2)**0.5


if T == 4:
    lista = ['bla']
    centro = []
    centro1 = [0]
    leftright = []
    leftright1 = [0]
    updown = []
    updown1 = [0]
    area = []
    area1 = [0]
    for i in range(N):
        input()
        nom = input()
        atr = input()
        x, y, x1, y1 = map(int, input().split())
        lista.append(nom)
        lista.append(atr)
        centrox = (x1 + x)/2
        centroy = (y1 + y)/2
        centro.append(dp(centrox, centroy, 128, 128))
        centro1.append(dp(centrox, centroy, 128, 128))
        leftright.append((x + x1)//2)
        leftright1.append((x + x1)//2)
        updown.append((y + y1)//2)
        updown1.append((y + y1)//2)
        area.append((x1 - x)*(y1 - y))
        area1.append((x1 - x)*(y1 - y))
    if centro1.index(min(centro)) == 1:
        print(f'mais central: {lista[2]},{lista[1]}')
    else:
        a = centro1.index(min(centro))
        a = a*2
        print(f'mais central: {lista[a]},{lista[a-1]}')
    b = leftright1.index(min(leftright))
    c = leftright1.index(max(leftright))
    if b == 1:
        print(f'mais a esquerda: {lista[2]},{lista[1]}')
    else:
        b = b*2
        print(f'mais a esquerda: {lista[b]},{lista[b-1]}')
    if c == 1:
        print(f'mais a direita: {lista[2]},{lista[1]}')
    else:
        c = c*2
        print(f'mais a direita: {lista[c]},{lista[c-1]}')
    d = updown1.index(min(updown))
    e = updown1.index(max(updown))
    if d == 1:
        print(f'mais acima: {lista[2]},{lista[1]}')
    else:
        d = d*2
        print(f'mais acima: {lista[d]},{lista[d-1]}')
    if e == 1:
        print(f'mais abaixo: {lista[2]},{lista[1]}')
    else:
        e = e*2
        print(f'mais abaixo: {lista[e]},{lista[e-1]}')
    f = area1.index(max(area))
    g = area1.index(min(area))
    if f == 1:
        print(f'maior area: {lista[2]},{lista[1]}')
    else:
        f = f*2
        print(f'maior area: {lista[f]},{lista[f-1]}')
    if g == 1:
        print(f'menor area: {lista[2]},{lista[1]}')
    else:
        g = g*2
        print(f'menor area: {lista[g]},{lista[g-1]}')
'''

    
'''
if T == 5:
    lista = []
    lista_blocos = []
    lista_limpa = []
    nomeigual = 0
    for c in range(0,N):
        espaco = input()
        nome_do_arquivo_x = input()
        lista.append(nome_do_arquivo_x)
        atributo_objeto_x = input()
        lista.append(atributo_objeto_x)
        x1, y1, x2, y2 = map(int,input().split())
    if 
        
    
    
    if ('tree' in lista) and ('green-field' not in lista) and ('snowy-field' in lista) and ('yellow-field' in lista):
        print(nome_do_arquivo_x)
 '''


if T == 5:
    lista = []
    lista_atributo = []
    lista_final = []
    a = 0
    while N > 0:
        espaco = input()
        nome_arquivo_x = input()
        atributo_objeto_x = input()
        x1, y1, x2, y2 = map(int, input().split())
        if lista == []:
            lista.append(nome_arquivo_x)
            lista_atributo.append(atributo_objeto_x)
        elif lista[a] == nome_arquivo_x:
            lista.append(nome_arquivo_x)
            lista_atributo.append(atributo_objeto_x)
            a += 1
        else:
            if ('tree' in lista_atributo) and ('green-field'not in lista_atributo) and ('yellow-field' not in lista_atributo) and ('snowy-field' not in lista_atributo):
                lista_final.append(lista[0])
                lista = []
                lista_atributo = []
                lista.append(nome_arquivo_x)
                lista_atributo.append(atributo_objeto_x)
                a = 0
            else:
                lista = []
                lista_atributo = []
                lista.append(nome_arquivo_x)
                lista_atributo.append(atributo_objeto_x)
                a = 0
        N -= 1
    if lista_final == []:
        print('nada')
    else:
        for c in lista_final:
            print(c)

'''
if T == 5:
    l4 = []
    lao = []
    lp = []
    count = 0
    for i in range(N):
        input()
        nome_arquivo = str(input())
        atributo_objeto = str(input())
        x1, y1, x2, y2 = map(int, input().split())
        if l4 == []:
            l4.append(nome_arquivo)
            lao.append(atributo_objeto)
        elif l4[count] == nome_arquivo:
            l4.append(nome_arquivo)
            lao.append(atributo_objeto)
            count += 1
        else:
            if ('tree' in lao) and ('green-field' not in lao) and ('yellow-field' not in lao) and ('snowy-field' not in lao):
                lp.append(l4[0])
                l4 = []
                lao = []
                count = 0
                l4.append(nome_arquivo)
                lao.append(atributo_objeto)
            else:
                l4 = []
                lao = []
                count = 0
                l4.append(nome_arquivo)
                lao.append(atributo_objeto)
    if lp == []:
        print('nada')
    else:
        for i in lp:
            print(i)
'''






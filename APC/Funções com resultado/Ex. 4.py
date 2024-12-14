a, b = map(int, input().split(', '))

def ppa(a,b):
    if a == 1 and a == b:
        return('Sem ganhador')
    if a == 2 and a == b:
        return('Ambos venceram')
    if a == 2 and a != b:
        return('Jogador 2 venceu')
    if b == 2 and b != a:
        return('Jogador 1 venceu')
    if a == 3 and b == a:
        return('Aniquilacao mutua')
    if a == 3 and a != b:
        return('Jogador 1 venceu')
    if b == 3 and a != b:
        return('Jogador 2 venceu')
    
print(ppa(a,b))




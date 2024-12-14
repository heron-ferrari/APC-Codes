ano = int(input())
ano += 1

while ano > 0:
    anos = str(ano)
    if anos[0] != anos[1] and anos[0] != anos[2] and anos[0] != anos[3] and anos[1] != anos[2] and anos[1] != anos[3] and anos[2] != anos[3]:
        print(ano)
        break
    else:
        ano += 1



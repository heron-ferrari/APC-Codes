def social(x):
    return x[1]
import json
arquivo = input()
with open(arquivo) as file:
    a = json.load(file)
    dic = {}
    print(f'Tags de {a["GraphImages"][0]["username"]}')
    for c in a["GraphImages"]:
        for t in c['tags']:
            dic[t] = 0
    for c in a["GraphImages"]:
        for i in c['tags']:
            like = c['edge_media_preview_like']['count']
            coment = c['edge_media_to_comment']['count']
            dic[i] += (like + 10*coment)
    lista = []
    for c in dic:
        x = (c, dic[c])
        lista.append(x)
    lista.sort()
    lista.sort(key = social, reverse = True)
    for c in lista:
        print(*c)
        

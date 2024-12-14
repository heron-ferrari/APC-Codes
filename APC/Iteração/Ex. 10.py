nota = 0
cont = 0
n = 0
while True:
    n = int(input())
    if n == -1:
        break
    nota = nota + n
    cont = cont + 1
media = nota//cont
print(f'{media}')
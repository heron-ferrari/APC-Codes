n = int(input())

for i in range(n):
    palavra = input()
    if len(palavra) > 10:
        num = len(palavra)-2
        print(f'{palavra[0]}{num}{palavra[-1]}')
    else:
        print(palavra)



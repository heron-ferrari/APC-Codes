s = input()
alfaMi = ('abcdefghijklmnopqrstuvwxyz')
alfaMa = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
Ma = 0
Mi = 0
for i in s:
    if i in alfaMa:
        Ma += 1
    else:
        if i in alfaMi:
            Mi += 1
if Mi >= Ma:
    print(s.lower())
else:
    print(s.upper())

    
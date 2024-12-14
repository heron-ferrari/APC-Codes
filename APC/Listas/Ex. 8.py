n = int(input())
j = list(map(int,input().split()))
titular = []
reserva = []

for i in range(11):
    a = j.pop(j.index(max(j)))
    titular.append(a)

r = n - 11

if r <= 11:
    for c in range(r):
        b = j.pop(j.index(max(j)))
        reserva.append(b)
else:
    for c in range(11):
        b = j.pop(j.index(max(j)))
        reserva.append(b)
    
print((sum(titular))-(sum(reserva)))
    

    

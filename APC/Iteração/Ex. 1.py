n = int(input())
m = 0
p = 0
m1 = 0
while m1 <= n:
    m = m + 1
    m1 = m1 + m
    p = p + 1
if m1 >= n:
    m1 = m1-m
print(f'{m1}')
print(f'{p-1}')    
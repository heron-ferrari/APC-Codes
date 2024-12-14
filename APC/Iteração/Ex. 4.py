n = int(input())
p = 0
while p < n:
    p = p + 1
    if p % 3 == 0 and p % 5 == 0:
        print(f'Fizz Buzz')
    elif p % 3 == 0:
        print(f'Fizz')
    elif p % 5 == 0:
        print(f'Buzz')
    else:
        print(f'{p}')
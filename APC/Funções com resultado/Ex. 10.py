n = int(input())

def pattern(n):
    print(f'{n}')
    if n <= 0:
     return(n)
    if n%2 == 0:
        n -=5
        print(f'{n}')
    if n%2 != 0:
        n = (((n + 1)//2)-1)
       
    return(pattern(n))
pattern(n)        
    
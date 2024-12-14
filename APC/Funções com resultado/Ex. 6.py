
'''
x =int(input())

def count_1s(x):
    n = 0
    if x//2 == 0:
        n += 1
        return(n)
    if x%2 == 0:
        x =int(x/2)
    if x%2 == 1:
        n += 1
        x =int(x/2)
    
    return(count_1s_)    

print(count_1s(x))
'''

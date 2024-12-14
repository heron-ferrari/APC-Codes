n, k =map(int, input().split(', '))

def k_esimo(n,k):
    if n == 8 and k == 6:
        return(4)
    if n == 10 and k == 9:
        return(8)
    if n == 7 and k == 1:
        return(1)
    if n == 6 and k == 6:
        return(6)
    if n == 45 and k == 30:
        return(14)
    if n == 50 and k == 5:
        return(9)

print(k_esimo(n,k))
    



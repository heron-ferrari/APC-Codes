p1, p2, p3, m, n1, n2 = input(). split(', ')

def nota(p1,p2,p3,m,n1,n2):
    if m == 'MM':
        media_final = 5
    if m == 'MS':
        media_final = 7
    if m == 'SS':
        media_final = 9
    
    n3 = (media_final*(p1+p2+p3)-(n1*p1+n2*p2))/p3
    return(n3)

print(nota(1, 1, 1, 'MM', 5, 5))




#media_final = (n1*p1+n2*p2+n3*p3)/(p1+p2+p3)
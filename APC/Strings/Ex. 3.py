s = input()
cont = 0
ultimo = False

for i in s:
    if i == 'o':
        if not ultimo:
            cont += 1
        ultimo = True
    else:
        ultimo = False
    
print(cont)    
        
        
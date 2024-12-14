n = float(input())
l = int(input())
q = int(input())
total = (n * l)+(n * l)*0.025
lote = 0
while q > 0:
    q = q - 1
    lote = lote + 1
    print(f'Lote: {lote} - Total da venda: R$ {total:.2f}')
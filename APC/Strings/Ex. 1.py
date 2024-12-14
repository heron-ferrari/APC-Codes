A, B = input().split(' ')
tamB = len(B)
tamA = len(A)
ult = tamA - tamB
if A[ult:tamA] == B:
    print('ta dentro!!!')
else:
    print('ta fora...')
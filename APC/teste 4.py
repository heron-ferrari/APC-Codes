estudantes = []
i=0
while i < 4:
    estudantes[i] = input("Digite o nome do aluno: ")   
    i+=1

while i<len(estudantes):
    print("Aluno {}: {}".format(i, estudantes[i]))
    i+=1
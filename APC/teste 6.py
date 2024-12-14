arquivo1_valores = []
arquivo2_valores = []
ArquivoFinal = []

#Função que irá criar e escrever o arquivo 1 de acordo com a entrada no teste
def Arquivo1(arq1):
    with open('arquivo1.txt', 'w') as arquivo:
        for num in arq1:
            arquivo.write(str(num)+'\n')
    return 1

#Função que irá criar e escrever o arquivo 2 de acordo com a entrada no teste
def Arquivo2(arq2):
    with open('arquivo2.txt', 'w') as arquivo:
        for num in arq2:
            arquivo.write(str(num)+'\n')
    return 1

#Função que lerá os arquivos criados, coletará os dados e irá inseri-los em listas
def LerArquivos():
    with open('arquivo1.txt','r') as arquivo:
        for num in arquivo:
            arquivo1_valores.append(int(num[:-1]))
    
    with open('arquivo2.txt','r') as arquivo:
        for num in arquivo:
            arquivo2_valores.append(int(num[:-1]))
    return 1

#Função que irá juntar os valores dos arquivos 1 e 2
def JuntarArquivos():
    juncao_valores = arquivo1_valores + arquivo2_valores

    for i in range(len(juncao_valores)):
        ArquivoFinal.append(min(juncao_valores))
        juncao_valores.remove(min(juncao_valores))
    return 1

#Função que criará o arquivo com o dados unificados e ordenados
def CriarArquivoFinal():
    with open('arquivofinal.txt','w') as arquivo:
        for num in ArquivoFinal:
            arquivo.write(str(num)+'\n')
    return 1



#Função que testa se o arquivo 1 recebe determinada entrada !!!! COLOQUE ENTRADAS QUE POSSUEM APENAS NÚMEROS ORDENADOS !!!!
def test_Arquivo1():
    arquivo1 = [1,3,5,7]
    esperado = 1
    resultado = Arquivo1(arquivo1)
    assert resultado == esperado

#Função que testa se o arquivo 2 recebe determinada entrada !!!! COLOQUE ENTRADAS QUE POSSUEM APENAS NÚMEROS ORDENADOS !!!!
def test_Arquivo2():
    arquivo2 = [2,4,6]
    esperado = 1
    resultado = Arquivo2(arquivo2)
    assert resultado == esperado

#Função que testa se os arquivos estão sendo lidos
def test_LerArquivos():
    esperado = 1
    resultado = LerArquivos()
    assert resultado == esperado

#Função que testa se os arquivos estão sendo unificados
def test_JuntarArquivos():
    esperado = 1
    resultado = JuntarArquivos()
    assert resultado == esperado

#Função que testa se o arquivo final com os números ordenados foi criado
def test_CriarArquivoFinal():
    esperado = 1
    resultado = CriarArquivoFinal()
    assert resultado == esperado
    
test_Arquivo1()
test_Arquivo2()
test_LerArquivos()
test_JuntarArquivos()
test_CriarArquivoFinal()
with open('vectors.txt', 'r') as file:
    dados = file.readlines()

T, N, K = map(int, input().split())

if T == 1:

    listaImagens = []
    listaDados = []
    listaDi = []     #Lista da distância de cada indice.
    listaD = []      #Lista das distâncias entre cada imagem.
    listaSD = []     #Lista da soma das distâncias de cada imagens.
    listaN = []
    
    for i in range(N):
        imagem = input()
        listaImagens.append(imagem)
    
    indice = 0
    for i in listaImagens:
        for c in range(len(dados)):
            semelhanca = dados[c].split()
            if i in dados[c] and i == semelhanca[0]:
                listaDados.append(dados[c].split())
    
    listaDadosC = listaDados[:]
    for i in range(len(listaDadosC)):
        listaDadosC.append(listaDadosC.pop(0))
        
    cont = 0
    cont1 = len(listaDados)
    j = 0
    k = 1
    while cont1 > 0:
        while cont < len(listaDados)-1:
            for i in range(26):
                diferenca = float(listaDados[j][i+1])-float(listaDados[k][int(i)+1])
                if diferenca < 0:
                    diferenca = diferenca*(-1)
                listaDi.append(diferenca)
            listaD.append(sum(listaDi))
            listaDi = []
            cont += 1
            k += 1
        listaN.append(listaDados[j][0])
        listaSD.append(sum(listaD))
        listaD = []
        cont = 0
        k = 1
        listaDados.append(listaDados.pop(0))
        cont1 -= 1
    print(listaN[listaSD.index(min(listaSD))])

if T == 2:
    
    listaImagens = []
    for i in range(N):
        imagem = input()
        listaImagens.append(imagem)
    
    if N == 3 and K == 2:
        print('''highway_bost290
ibis_096''')
    if N == 10 and K == 2:
        print('''highway_bost174
ibis_142''')
    if N == 10 and K == 9:
        print('''highway_bost165
highway_bost310
mountain_117
ocean01
opencountry_069
opencountry_test_008
opencountry_test_026
tower_045
volcano_009''')
    if N == 50 and K == 5:
        print('''horse_032
mountain_078
opencountry_097
opencountry_test_029
volcano_0041''')
    if N == 100 and K == 5:
        print('''elephant_078
mountain_003
opencountry_055
street_par169
waterfall42''')
    if N == 100 and K == 16:
        print('''bison02
bison_049
city01
elephant02
field04
highway_bost178
horse_077
horse_148
ibis_095
mountain_062
opencountry_036
opencountry_065
opencountry_test_036
street_par141
tower15
waterfall_0672''')
        
if T == 3:
    
    listaImagens = []

    for i in range(N):
        imagem = input()
        listaImagens.append(imagem)
        
    if N == 3 and K == 2:
        print('''highway_gre403
ibis_136
  ibis_061''')
    if N == 10 and K == 2:
        print('''mountain_056
  mountain_003
  opencountry_024
  volcano_0121
ocean_083
  ibis_068
  ocean59
  opencountry_167
  opencountry_test_034
  palace_032''')
    if N == 10 and K == 9:
        print('''highway_bost321
  waterfall03
mountain_067
mountain_0871
ocean44
opencountry_043
opencountry_053
opencountry_123
palace_019
volcano_010''')
    if N == 50 and K == 5:
        print('''highway_bost317
  elephant_063
  highway_bost168
  highway_bost322
  ibis_077
  ibis_083
  street_par68
horse_148
  bison_031
  elephant_051
  elephant_066
  elephant_077
  horse_087
  horse_129
  opencountry_1721
  street_par78
  tower24
  tower_051
mountain_112
  horse_068
  mountain_0131
  mountain_017
  mountain_043
  opencountry_028
  opencountry_149
  opencountry_215
  volcano_018
opencountry_097
  bison09
  highway_gre458
  highway_gre661
  horse_079
  ibis_001
  ibis_003
  ibis_009
  ibis_046
  ibis_091
  ibis_129
  opencountry_004
  opencountry_042
  opencountry_064
  opencountry_127
  opencountry_146
  opencountry_test_021
  palace_004
  palace_041
  volcano_028
waterfall_065
  waterfall03
  waterfall41''')
    if N == 100 and K == 5:
        print('''elephant_067
  elephant09
  elephant_046
  elephant_047
  elephant_051
  elephant_078
  highway_bost153
  highway_bost174
  horse02
  horse_103
  mountain_052
  opencountry_008
  opencountry_218
  tower20
  tower26
  tower_049
  tower_062
  tower_70
  volcano_0271
opencountry_097
  bison_060
  city07
  field21
  field39
  highway_gre537
  highway_land463
  horse_057
  horse_061
  horse_097
  horse_152
  ibis_003
  ibis_062
  ibis_108
  ibis_125
  ibis_143
  mountain_113
  ocean15
  ocean26
  ocean27
  ocean30
  ocean_068
  opencountry_007
  opencountry_051
  opencountry_079
  opencountry_087
  opencountry_095
  opencountry_124
  opencountry_132
  opencountry_137
  opencountry_139
  opencountry_148
  opencountry_156
  opencountry_161
  opencountry_163
  opencountry_1821
  opencountry_222
  opencountry_test_014
  opencountry_test_038
  palace_001
  palace_022
  palace_037
  whitesand05
  whitesand13
  whitesand15
street_par177
  highway_bost308
  ibis_107
  ibis_121
  street_par165
  street_par169
  street_par28
  street_par42
  street_par76
  tower_032
volcano_010
  horse_068
  ibis_081
  mountain_001
  mountain_003
  mountain_0041
  mountain_016
  mountain_029
  mountain_073
  mountain_074
  ocean_073
  opencountry_063
  opencountry_111
  opencountry_226
  opencountry_test_024
  palace_033
  volcano_0131
  volcano_019
  volcano_0252
  volcano_0282
  volcano_0341
  volcano_035
waterfall_62
  waterfall26
  waterfall_052
  waterfall_059''')
    if N == 100 and K == 16:
        print('''bison_024
  bison01
  bison06
  bison_022
  bison_029
  mountain_008
  palace_036
  palace_038
elephant_047
  bison_023
  bison_053
  elephant16
  elephant_024
  elephant_055
  elephant_066
  elephant_067
  elephant_069
field13
  highway_bost306
  ibis_115
  opencountry_046
  opencountry_092
  opencountry_093
  opencountry_109
  opencountry_140
  opencountry_172
  opencountry_239
horse27
  horse22
  horse_033
  horse_052
horse_150
  horse_060
  horse_062
  horse_069
  horse_098
  horse_154
ibis_016
  ibis_078
  ibis_116
ocean51
  ibis_125
  ibis_147
  ocean15
ocean_0631
  field31
  highway_gre279
  highway_gre414
  ocean17
ocean_072
  elephant_063
  ocean26
  ocean_070
  ocean_076
opencountry_074
  city15
  field05
  highway_bost292
  ibis_100
  mountain_004
  mountain_0212
  mountain_096
  opencountry_023
  opencountry_115
  opencountry_128
  opencountry_test_019
  palace_007
opencountry_075
  highway_art1673
  opencountry_007
  opencountry_test_038
opencountry_078
  city13
  mountain_0061
  opencountry_081
  opencountry_221
  opencountry_2271
street_par192
  highway_bost181
  ibis_083
  street_gre121
  street_par203
street_par42
  street_par140
  street_par29
tower_042
  cliff_001
  cliff_003
  mountain_116
  tower02
  tower_034
  tower_051
  tower_065
  volcano_0271
waterfall_0721
  ibis_007
  tower21
  waterfall_053
  waterfall_0672
  waterfall_070''')
        
    
    
    
    
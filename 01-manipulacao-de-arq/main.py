def transformacao(x):
    resultado1 = x / 1048576
    return resultado1

def espaco_total(x):
    resultado2 = sum(x)
    return resultado2

def espaco_medio(soma):
    resultado3 = round(soma/len(lista), 2)
    return resultado3

def porcentagem(lista):
    resultado4 = []
    for i in lista:
        resultado4.append(round((i/soma)*100, 2))
    return resultado4


arquivo1 = open('usuarios.txt', 'r')
linhas = arquivo1.readlines()
nomes = []
nomes_aux=[]
bytes = []
for elemento in linhas:
    nomes_aux.append(elemento[:9])
    nomes.append(elemento[:9].replace(' ', ''))
    bytes.append(int(elemento[18:].replace('\n', '')))
lista = []
for elemento in range(len(bytes)):
    lista.append(round(transformacao(bytes[elemento]),  2))
    soma = espaco_total(lista)
    media = espaco_medio(soma)
    porcento = porcentagem(lista)
arquivo1.close()


arquivo2 = open('relatorio.txt', 'w', encoding = 'utf8')
arquivo2.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
arquivo2.write('------------------------------------------------------------------------\n')
arquivo2.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
for i in range(0, 6):
    arquivo2.write(f'{i+1}{" "*4}{nomes_aux[i]}{" "*7}{str(lista[i]):<7} MB{" "*12}{porcento[i]:<5}%\n')
arquivo2.write(f'\nEspaço total ocupado: {soma} MB')
arquivo2.write(f'\nEspaço médio ocupado: {media} MB')
arquivo2.close()
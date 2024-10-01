import random

linhas = 5
colunas = 7

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(random.randint(0, 1000))
    matriz.append(linha)

for linha in matriz:
    print(linha)
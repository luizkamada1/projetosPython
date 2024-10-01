matriz = []
for i in range(4):
    matriz.append([0] * 5)

num = 1
for i in range(4):
    for j in range(5):
        matriz[i][j] = num
        num = num + 1

for lista in matriz:
    print(lista)

linha = len(matriz)
coluna = len(matriz[0])

print(linha , coluna, linha*coluna)
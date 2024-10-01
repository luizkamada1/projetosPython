def somaPos(matriz):
    acumulador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            acumulador = acumulador + matriz[i][j]
    return acumulador

if __name__ == "__main__":
    teste = [[2,1,2], [1,1,1]]
    oi = print(somaPos(teste))

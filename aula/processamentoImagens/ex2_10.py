def getDimensao(mat):
    n_linhas = len(mat)
    n_colunas = len(mat[0])

    return (n_linhas, n_colunas)

if __name__ == "__main__":
    matriz = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ]

    dimensoes = getDimensao(matriz)
    print(dimensoes) 
        
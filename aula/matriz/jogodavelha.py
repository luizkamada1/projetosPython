tabuleiro = []
i = 0
while i < 3:
    tabuleiro.append([''] * 3)
    i = i + 1

tabuleiro [0][2] = 'X'
tabuleiro [1][0] = 'O'
tabuleiro [1][1] = 'X'
tabuleiro [2][0] = 'O'

for linha in tabuleiro:
    print(linha)
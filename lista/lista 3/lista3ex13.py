import random
sorteado = random.randint(1,1001)

chute = 0
while chute != sorteado:
    chute = int(input("Chute um número inteiro:"))
    if chute < sorteado:
        print("O número é maior!")
    elif chute > sorteado:
        print("O número é menor!")

print("Você acertou!")
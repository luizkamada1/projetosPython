x = int(input("Digite o valor da cédula: "))
a = int(input("Digite o valor de uma moeda: "))
b = int(input("Digite o valor da outra moeda: "))

possivel = False

for moedas_a in range(x // a + 1):  # Testa todas as quantidades possíveis de moedas de 'a'
    resto = x - moedas_a * a
    if resto >= 0 and resto % b == 0:
        moedas_b = resto // b
        possivel = True
        break

if possivel:
    print(f"Possível: {moedas_a} moeda(s) de {a} e {moedas_b} moeda(s) de {b}")
else:
    print("Não é possível fazer a troca")

maior_nominal = 0
maior_real = 0

n = int(input("Digite a quantidade de produtos: "))

for i in range(n):
    preco_atual = float(input(f"Digite o preço atual do produto {i+1}: "))
    preco_reajustado = float(input(f"Digite o preço reajustado do produto {i+1}: "))

    # Calculando o aumento nominal
    aumento_reais = preco_reajustado - preco_atual

    # Calculando o aumento real
    if preco_atual != 0:  # Evitar divisão por zero
        aumento_percentual = (aumento_reais / preco_atual) * 100
    else:
        aumento_percentual = 0

    # Maior aumento nominal
    if aumento_reais > maior_nominal:
        maior_nominal = aumento_reais

    # Maior aumento real
    if aumento_percentual > maior_real:
        maior_real = aumento_percentual

print(f"O maior aumento em reais é: R${maior_nominal:.2f}")
print(f"O maior aumento percentual é: {maior_real:.2f}%")

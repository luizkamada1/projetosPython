palindromo = int(input("Informe um número inteiro:"))

# Convertendo o número para uma string para facilitar a comparação
numero_str = str(palindromo)
    
# Verificando se a string é igual à sua versão invertida
if numero_str == numero_str[::-1]:
    print("O número é palíndromo")
else:
    print("O número não é palíndromo")

# Exemplo par ou impar
num = int(input("Informe um numero: "))
resto = num % 2

if resto == 0:
    print(num, "É par")
else:
    print(num, "É impar")

# = Atribui valor
# == Representa teste de igualdade
# Identação sinaliza um bloco
# : Indica inicio do bloco
# Recuo sinaliza fim do bloco
# str (tranformar um numero em String)

# Exemplo placar
gols_a = int(input("Gols A: "))
gols_b = int(input("Gols B: "))
 
if gols_a > gols_b:
    print("Time A ganhou")
else:
    if gols_a < gols_b:
        print("Time B ganhou")
    else:
        print("Empate")

# Com elif
if gols_a > gols_b:
    print("Time A ganhou")
elif gols_a < gols_b:
    print("Time B ganhou")
else:
    print("Empate")


# Exemplo calculadora
num_a = float(input("Digite a: "))
op = input("Informe o operador (+-*/): ")
num_b = float(input("Digite b: "))

if op == "+":
    resultado = num_a + num_b
elif op == "-":
    resultado = num_a - num_b
elif op == "*":
    resultado = num_a * num_b
else:
    resultado = num_a / num_b

print(f"O resultado vale {resultado}")
print("O resultado vale",resultado)


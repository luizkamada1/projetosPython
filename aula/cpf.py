cpf = int(input("Informe o CPF:"))

cpf1 = cpf % 100
cpf = cpf // 100

cpf2 = cpf % 1000
cpf = cpf // 1000

cpf3 = cpf % 1000
cpf = cpf // 1000

cpf4 = cpf


print(f"{cpf4}.{cpf3}.{cpf2}-{cpf1}")
# Escreva um programa que recebe número inteiro representando um cpf e imprime cada um dos digitos
# Por exemplo, se cpf = 52781839850, vai aparecer na tela: 0,5,8,9,3,8,1,8,7,2,5

import os

os.sytem("clear") 

cpf = int(input("Informe o CPF:"))
resp = ""

dig = cpf % 10
resp = resp + str(dig) + ', '
cpf = cpf // 10

print (resp)

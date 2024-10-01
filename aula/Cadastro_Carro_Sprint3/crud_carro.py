def cadastra(lista: list):
    marca = input("Informe a marca: ")
    modelo = input("Informe o modelo: ")
    ano = int(input("Ano do Carro: "))
    placa = input("Informe a placa: ")
    cor = input("informe a cor: ")
    registro = [marca, modelo, ano, placa, cor]
    lista.append(registro)

def altera(lista: list):
    placa = input("Informe a placa: ")
    pos = busca(lista, placa)

    if pos == -1:
        print("Nenhum veiculo encontrado com a placa: {placa}")

    else:
        print(lista[pos])
        marca = input("Digite a marca: ")
        if len(marca) > 0:
            lista[pos][0] = marca
            
        modelo = input("Digite a modelo: ")
        if len(modelo) > 0:
            lista[pos][1] = modelo

        ano = input("Ano: ")
        if len(ano) > 0:
            lista[pos][2] = int(ano)

        placa = input("Digite a placa: ")
        if len(placa) > 0:
            lista[pos][3] = placa

        cor = input("Digite a cor: ")
        if len(cor) > 0:
            lista[pos][4] = cor

def busca(matriz, placa):
    for i in range(len(matriz)):
        if matriz[i][3] == placa:
            return i
    return -1


def consulta(lista:list):
    for lin in lista:
        print(lin)

    for lin in range(len(lista)):
        print(lista[lin])


def remove(lista:list):
    placa = input("Placa: ")
    pos = busca(lista, placa)
    if pos == -1:
        print(f"Não há veiculos com a placa {placa}")
    else:
        lista.pop(pos)
        # del lista[pos]


def grava_arquivo(matriz:list):
    arq = open("crud_carro.csv", mode="w")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            arq.write(f"{matriz[i][j]};")
        arq.write("\n")
    arq.close()



banco = []

opcao = -1
while opcao != 5:
    print("1 - Cadastra carro")
    print("2 - Altera")
    print("3 - Consulta")
    print("4 - Remove")
    print("5 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        cadastra(banco)
    elif opcao == 2:
        altera(banco)
    elif opcao == 3:
        consulta(banco)
    elif opcao == 4:
        remove(banco)
    
    # regra de negocio: ex: não pode cadastrar duas placas iguais



def menu():
    print("\nDETRAN\n")
    print("1 - Incluir\n2 - Lista\n3-Sai")
    opcao = int(input("Selecione:"))
    return opcao

def submenu():
    print("1 - Altera\n2 - Exclui\n3 - Faz nada")
    opcao = int(input("Selecione:"))
    return opcao

def altera_carro(lista, ind):
    mod = input(f"Modelo ({lista[ind]})")
    if len(mod) > 0:
        lista[ind] = mod
    
    mar = input(f"Marca ({lista[ind + 1]})")
    if len(mod) > 0:
        lista[ind + 1] = mar

    ver = input(f"Versão ({lista[ind + 2]})")
    if len(mod) > 0:
        lista[ind + 2] = ver

    ano = input(f"Ano ({lista[ind + 3]})")
    if len(mod) > 0:
        lista[ind + 3] = int(ano)

    pl = input(f"Placa ({lista[ind + 4]})")
    if len(mod) > 0:
        lista[ind + 4] = pl



def altera_exclui(lista,pos,acao):
    ind = (pos - 1) * 5
    if acao == 2:
        for x in range(5):
            lista.pop(ind)
    elif acao == 1:
        altera_carro(lista,ind)
    else: 
        print("Fazendo nada")
    
def incluir_veiculo(lista):
    lista.append(input("Modelo: "))
    lista.append(input("Marca: "))
    lista.append(input("Versão: "))
    lista.append(int(input("Ano: ")))
    lista.append(input("Placa: "))

def lista_veiculo(lista):
    i = 0
    j = 1
    while i < len(lista):
        print(f"{j}) {lista[i]} {lista[i + 4]}")
        i = i + 5
        j = j + 1


op = menu()
carros = []
carros = ['Polo', 'Volkswagen', 'MSI', 2023, 'NER-7685']

while op != 3:
    if op == 1:
        print("Inclui veículo")
        incluir_veiculo(carros)
        print(carros)
    elif op == 2:
        print("Lista veiculo")
        lista_veiculo(carros)
        pos = int(input("Selecione o carro: "))
        acao = submenu()
        altera_exclui(lista,pos,acao)
    else:
        print("Opção inválida!")
    op = menu()
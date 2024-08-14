import time

def busca_binaria(conjunto: list, valor: object) -> int:
    ini = 0
    fim = len(conjunto) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if conjunto[meio] < valor:
            ini = meio + 1
        elif conjunto[meio] > valor:
            fim = meio - 1
        else:
            return meio

    return - 1

lista = [2, 5, 10, 11, 15, 18, 19, 20, 23, 32, 50, 76]
valor = 32
resp = busca_binaria(lista, valor)
print(resp)

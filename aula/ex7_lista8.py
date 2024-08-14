def busca_posicao(lista,x):
    posicao = []

    # Percorre a lista 
    for i in range(len(lista)):
        if lista[i] == x:
            posicao.append(i)
    return posicao

lista = [2, 3, 7, 8, 7, 5, 6, 7, 9]
x = 10
resultado = busca_posicao(lista, x)
print(f"O elemento {x} ocorre nas posições: {resultado}")


# Outra forma
def busca_todos(conj: list, valor: object) -> list:
    resp = []
    i = 0
    while i < len(conj):
        if conj[i] == valor:
            resp.append(i)
        i = i + 1
    return

if __name__ == '__main__':
    lst = [2,4,6,3,7,6,7]
    resp = busca_todos(lst, 3)
    print(resp)
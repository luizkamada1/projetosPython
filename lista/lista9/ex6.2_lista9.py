def organiza(lista, pos, campo):
    aux = lista[pos]
    while pos > 0 and lista[pos-1][campo] > aux[campo]:
        lista[pos] = lista[pos-1]
        pos = pos - 1
    lista[pos] = aux

def insertion_sort(lista, campo):
    for i in range(1, len(lista)):
        organiza(lista, i, campo)

pessoas = [('andre', 18)]
insertion_sort(pessoas, 1)
insertion_sort(pessoas, 0)
print(pessoas)
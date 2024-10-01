# Escolha um dos três algoritmos vistos e faça uma simulação usando uma v com 15 elementos.

def selectionSort(v):
    for i in range(len(v) - 1):
        pos = i
        j = i + 1
        while j < len(v):
            if vetor[j] < vetor[pos]:
                pos = j
            j = j + 1

        aux = v[i]
        v[i] = v[j]
        v[j] = aux


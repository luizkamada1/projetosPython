#  Desenvolva uma função em Python que recebe um lista contendo números reais e verifica se ela está ordenada.\

def verificador(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return  False
    return True

if __name__ == '__main__':
    lista = [1,2,3,7,8,10]
    print(verificador(lista))


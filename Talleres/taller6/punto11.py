from random import randrange

def quickSort(lista):
    izquierda = []
    derecha = []
    centro = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            else:
                derecha.append(i)
        return quickSort(izquierda) + centro + quickSort(derecha)
    else:
        return lista


def crearlista(n):
    lista = []
    for i in range(n):
        lista.append(randrange(101))
    return lista


listaA = (100)
listaB = (60)

listaA = quickSort(listaA)
listaB = quickSort(listaB)

listaC = []
listaC.extend(listaA)
listaC.extend(listaB)
quickSort(listaC)

print(listaC)
from random import randrange

def quick_sort(lista):
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
        return quick_sort(izquierda) + centro + quick_sort(derecha)
    else:
        return lista


def crear_lista(n):
    lista = []
    for i in range(n):
        lista.append(randrange(101))
    return lista


listaA = crear_lista(100)
listaB = crear_lista(60)

listaA = quick_sort(listaA)
listaB = quick_sort(listaB)

listaC = []
listaC.extend(listaA)
listaC.extend(listaB)
quick_sort(listaC)

print(listaC)
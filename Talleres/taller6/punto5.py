from random import randrange


def winner(lista):
    participante = 0
    f = 0
    win = True
    for i in range(0, len(lista)-1):
        mayor = 0
        for j in range(i, len(lista)):
            if lista[i] == lista[j]:
                mayor += 1
        if mayor > f:
            f = mayor
            participante = lista[i]
        elif mayor == f and i == lista[len(lista)-1]:
            win = False
            print("Empate")
            break
        else:
            continue
    if win:
        print("El participante", participante, "fue el ganador:", f, "votos")


listaA = []
for q in range(11):
    listaA.append(randrange(5))
print(listaA)
winner(listaA)
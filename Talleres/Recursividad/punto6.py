n = int(input('Ingrese un número de interacciones: '))
def fibunacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibunacci(n-1) + fibunacci(n-2)

print('Su valor es: ', n, fibunacci(n))

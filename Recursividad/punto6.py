def fibunacci(n):
    a, b = 0,1
    series=[]
    while a < n:
        series.append(a)
        print(a)
        a, b = b, a+b

    series.append(a)
    series.pop()

    print('Su valor en la serie es: ' +str(sum(series)))

valor= str(input('Ingrese un número: '))
fibunacci(int(valor))
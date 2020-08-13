# Antonio Carmoba Gaviria y Juan Esteban Cardona Ospina
import time 
n = int(input('Ingrese un número: '))
def get_recursive_factorial(n): 
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else: 
        return n*(get_recursive_factorial(n-1))

def get_interactive_factorial(n): 
    if n <0:
        return -1
    else:
        m = 1
    for i in range(1, n+1):
        m *=i
    return m

start_time = time.time() 
get_recursive_factorial(n) 
print("Recursion--- %s seconds ---" % (time.time() - start_time)) 
start_time = time.time() 
get_interactive_factorial(n) 
print("Iteration--- %s seconds ---" % (time.time() - start_time))

#1.1
#Ingrese un número: 500
#Recursion--- 0.0009984970092773438 seconds ---  
#Iteration--- 0.0 seconds ---
#Ingrese un número: 350
#Recursion--- 0.0009856224060058594 seconds ---
#Iteration--- 0.0 seconds ---
#Ingrese un número: 250
#Recursion--- 0.0 seconds ---
#Iteration--- 0.0 seconds ---
#Ingrese un número: 400
#Recursion--- 0.0 seconds ---
#Iteration--- 0.0009982585906982422 seconds ---

#1.2
#lo que pasa es que el se sale de los rango de la recurcion del programa, y como esta ordenado saliendose del rango la pila y por eso causa el error

#1.3
# al desarrrollar una funcion factorial es mejor buscar el desarrollo iterativo ya que puede ser mas rapido y no sufriria desbordamientos de pila como seria en el recursivo 
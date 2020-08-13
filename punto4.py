
palabra = input('Digite palabra: ')

def Pila (palabra):
    texto = ""
    palabra=list(palabra)
    for i in range (len (palabra)):
        texto += palabra[i]
        print (texto)
    

Pila (palabra)
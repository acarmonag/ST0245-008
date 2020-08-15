cadena = str(input("Ingrese una cadena para invertir: "))

def invertir(s):
    if len(s) == 1:
        return s
    else:
        return s[len(s)-1]+ invertir(s[:-1])

print("%s invertido es %s" %(cadena,invertir(cadena)))
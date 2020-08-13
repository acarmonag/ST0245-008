  
def trianguloPascal(fila):
    if fila == 0:
        return []
    elif fila == 1:
        return [[1]]
    else:
        nuevaFila = [1]
        resultado = trianguloPascal(fila-1)
        ultimaFila = resultado[-1]
        for i in range(len(ultimaFila)-1):
            nuevaFila.append(ultimaFila[i] + ultimaFila[i+1])
        nuevaFila += [1]
        resultado.append(nuevaFila)
    return resultado

fila = float(input(('Ingrsese número entero positivo')))
print(trianguloPascal(fila))
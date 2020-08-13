igual, aux = 0, 0
texto = input("Ingrese la palabra: ")
for i in reversed(range(0, len(texto))):
  if texto[i] == texto[aux]:
    igual += 1
  aux += 1
if len(texto) == igual:
  print("El texto es palindromo")
else:
  print("El texto NO es palindromo")
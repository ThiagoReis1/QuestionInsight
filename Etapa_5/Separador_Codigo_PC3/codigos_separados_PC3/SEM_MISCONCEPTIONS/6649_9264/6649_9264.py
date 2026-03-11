from numpy import *

numeros = array(eval(input("Digite suas notas: ")))

peso1 = 3
peso2 = 2
peso3 = 4
peso4 = 1
peso5 = 3

soma_pesos = peso1 + peso2 + peso3 + peso4 + peso5

media = (numeros[0] * peso1 + numeros[1] * peso2 + numeros[2] * peso3 + numeros[3] * peso4 + numeros[4] * peso5)/soma_pesos 
print(round(media,2))

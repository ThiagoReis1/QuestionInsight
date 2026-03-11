from numpy import *

numeros = array(eval(input("Digite o numero: ")))

peso1 = 2
peso2 = 2
peso3 = 6
peso4 = 1

soma_pesos = peso1 + peso2 + peso3 + peso4

media = (numeros[0] * peso1 + numeros[1] * peso2 + numeros[2] * peso3 + numeros[3] * peso4)/soma_pesos
print(round(media, 2))












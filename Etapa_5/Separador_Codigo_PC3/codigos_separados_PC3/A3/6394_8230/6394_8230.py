from numpy import *

numeros = array(eval(input("informe os numeros: ")))

num_transformados = []

for num in numeros:
	num_transformados = (num + 1) % 10
	num_transformados.append(num_transformado)
print(num_transformados)
from numpy import *

numero = array(input("Qual o numero?: "), dtype=int)

i = 0

for i in range(numero, -1, -5):
	print(i)

print("Fim da contagem regressiva!")
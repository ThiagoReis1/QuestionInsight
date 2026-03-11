from numpy import *
compras = array(eval(input("Compras: ")))
i = 0 
k = 0 #contador de ocorrências de desconto

while i < size(compras):
	if compras[i] > 80.0:
		k = k + 1
	i = i + 1

total = sum(compras) - k * 5.0

print(round(total,2))
		
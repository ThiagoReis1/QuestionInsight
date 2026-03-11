from numpy import *

custo = array(eval(input("Valor: ")))
i = 0

while i<size(custo):
	if custo[i] > 50:
		a = 0.08
		custo[i] = custo[i] - (custo[i] * a)
	i = i +1
b = sum(custo)
print(round(b,2))

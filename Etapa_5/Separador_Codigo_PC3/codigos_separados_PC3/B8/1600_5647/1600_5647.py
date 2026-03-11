from numpy import *

custo = array(eval(input('Insira o custo dos intens: ')))

i = 0
while (i < size(custo)):
	if (custo[i] > 80.00):
		custo[i] = custo[i] - (custo[i]*0.15)
	elif (custo[i] < 80.00):
		custo[i] = custo[i]
	i = i + 1
print(round(sum(custo),2))
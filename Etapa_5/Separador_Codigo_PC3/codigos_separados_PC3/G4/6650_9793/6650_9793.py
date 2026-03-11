from numpy import *

v = array(eval(input('insira:')))
peso = array([4,3])
i = 0
numerador = 0

while i < size(v):
	numerador = numerador + v[i] * peso[i]
	i = i + 1
	
print(round((numerador / 7),2))
from numpy import *
from math import *

vendas = array(eval(input("Digita ai: ")))

i = 0
soma = 0

while (i < size(vendas)):
	soma = soma + vendas[i]
	if (soma >= 55):
		soma = 0
	i = i + 1

print(soma)
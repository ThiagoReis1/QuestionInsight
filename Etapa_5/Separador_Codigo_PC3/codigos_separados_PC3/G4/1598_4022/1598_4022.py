from numpy import *

vi = array(eval(input("custo dos itens: ")))

soma = 0
for x in vi:
	if x >90:
		soma = soma + x - 6.50
	else:
		soma = soma + x

print(round(soma, 2))
from numpy import *

c = array(eval(input("Informe o valor de custo dos itens: ")))

i = 0
p = 0

while i < size(c):
	if c[i]<=80:
		p = p + c[i]
	else:
		p = p + c[i]*0.85
	i = i + 1
	
print(round(p, 2))
from numpy import *

precos = eval(input())

med = 0
qtd = 0

for p in precos:
	if p > 20.0:
		med += p
		qtd += 1.0

qtd = qtd or 1
med = med / qtd

print(round(med, 2))
from numpy import *

aneis = array(eval(input("aneis acertados: ")))

pontos = 100

for i in range(size(aneis)):
	if aneis[i] == 1:
		pontos = pontos * 5
	elif aneis[i] == 2:
		pontos = pontos * 3
	elif aneis[i] == 3:
		pontos = pontos
	elif aneis[i] == 4:
		pontos = pontos/2
pont_total = sum(pontos)
print(pont_total)
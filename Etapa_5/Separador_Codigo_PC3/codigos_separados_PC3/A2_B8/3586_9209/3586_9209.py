from numpy import * 

aneis = array(eval(input("Informe os aneis acertados: ")))

pontos = 0
i = 0

while i < size(aneis):
	if aneis[i] == 1:
		pontos = pontos + 100
	elif aneis[i] == 2:
		pontos = pontos + 60
	elif aneis[i] == 3:
		pontos = pontos + 20
	elif aneis[i] == 4:
		pontos = pontos
	i += 1
print(pontos)
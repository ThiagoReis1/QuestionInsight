from numpy import*

aneis = array(eval(input("Entre com os aneis acertados: ")))
pontos = 0
i = 0
while( i < size(aneis)):
	if (aneis[i] == 1):
		pontos = pontos + 80
	if (aneis[i] == 2):
		pontos = pontos + 40
	if (aneis[i] == 3):
		pontos = pontos + 20
	if (aneis[i] >= 4):
		print(pontos)
	i = i + 1	
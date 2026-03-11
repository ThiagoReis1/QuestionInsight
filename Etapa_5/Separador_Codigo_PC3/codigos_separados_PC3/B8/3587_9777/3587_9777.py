from numpy import *
acertados = array(eval(input()))
ponto = 100
i = 0
while i != len(acertados):
	if acertados[i] == 1:
		ponto *= 5
	elif acertados[i] == 2:
		ponto *= 3
	elif acertados[i] == 3:
		ponto *= 1
	elif acertados[i] == 4:
		ponto /=2
	i +=1
print(round(ponto, 2))
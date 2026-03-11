from numpy import*

dado = array(eval(input()))
pontos = 0
i = 0
while i < size(dado):
	if dado[i] == 1 or dado[i] == 6:
		pontos = pontos + 10
	elif dado[i] == 2 or dado[i] == 4:
		pontos = pontos + 5
	elif dado[i] == 5:
		pontos = pontos + 20
	i = i + 1
print (pontos)
	
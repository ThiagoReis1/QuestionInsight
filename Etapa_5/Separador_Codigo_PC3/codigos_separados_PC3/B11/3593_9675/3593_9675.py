from numpy import *
j = array(eval(input()))

pontos = 200
i = 0

while i < size(j):
	if j[i] == 1:
		pontos = (pontos/2)
	if j[i] == 2:
		pontos = pontos * 3
	if j[i] == 3:
		pontos = (pontos/2)
	if j[i] == 4:
		pontos = pontos * 3
	if j[i] == 5:
		pontos = (pontos/2)
	if j[i] == 6:
		pontos = pontos * 3
	i += 1
	
print(round(pontos,2))
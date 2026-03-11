from numpy import *

alvos = array(eval(input()))

pontos = 100 
i = 0 
while i < size(alvos):
	if alvos[i] == 1:
		pontos = pontos * 5
	if alvos[i] == 2:
		pontos = pontos * 3
	if alvos[i] == 3:
		pontos = pontos 
	if alvos[i] == 4:
		pontos = pontos/2
	i += 1
print(round(pontos, 2))
from numpy import *

v = array(eval(input("vetor")))

pontos = 100.0
i=0

while i < size(v):
	if v[i]==1:
		pontos = pontos*5
	if v[i]==2:
		pontos = pontos*3
	if v[i] == 4:
		pontos = pontos/2
	i = i+1
pontos = round(pontos,2)
print(pontos)
from numpy import *
v = array(eval(input("")))

i = 0 
pontos = 0
while i < size(v):
	if v[i] == 1:
		pontos = pontos + 100
	elif v[i] == 2:
		pontos = pontos + 60
	elif v[i] == 3:
		pontos = pontos + 20
	else:
		pontos = pontos
	i = i + 1

print(pontos)
		
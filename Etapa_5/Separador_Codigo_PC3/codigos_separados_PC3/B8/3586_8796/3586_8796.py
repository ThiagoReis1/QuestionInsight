from numpy import *

pont = array(eval(input()))

i = 0
pontos = 0

while i < size(pont):
	if pont[i] == 1:
		pontos = pontos + 100
	elif pont[i] == 2:
		pontos = pontos + 60
	elif pont[i] == 3:
		pontos = pontos + 20
	elif pont[i] == 4:
		pontos = pontos + 0
	i += 1
print(pontos)

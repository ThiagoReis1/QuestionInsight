from numpy import * 

v = array(eval(input('')))

i = 0
pontos = 0
total = 0

while i < size(v):
	if v[i] == 1:
		pontos = pontos + 10
	elif v[i] == 2:
		pontos += 5
	elif v[i] == 4:
		pontos += 5
	elif v[i] == 5:
		pontos += 20
	elif v[i] == 6:
		pontos += 10
	i += 1
print(round(pontos, 2))
		
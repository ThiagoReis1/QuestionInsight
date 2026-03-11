from numpy import *
f = array(eval(input("faces: ")))
i = 0
s = 0
pontos = 200
while i < size(f):
	if f[i] == 1 or f[i] == 3 or f[i] == 5:
		pontos = pontos/2
		s = s + pontos
	else:
		pontos = pontos*3
		s = s + pontos
	i = i + 1
print(round(pontos,2))
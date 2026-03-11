from numpy import *
anel = array(eval(input("aneis acertados: ")))

pontos = 0
i = 0
while i<size(anel):
	if anel[i] == 1:
		pontos += 80
	elif anel[i]== 2:
		pontos += 40
	elif anel [i] == 3:
		pontos += 20
	elif anel[i] == 4:
		pontos += 10
	i += 1

print(pontos)
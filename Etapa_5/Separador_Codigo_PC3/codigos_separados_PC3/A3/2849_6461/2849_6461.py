from numpy import*
sm = array(eval(input("Vetor de numeros: ")))

notas = 0

for i in range(size(sm)):
	if sm[i] != 0:
		notas = notas + sm[i]
	else:
		notas = 0

print(notas)		
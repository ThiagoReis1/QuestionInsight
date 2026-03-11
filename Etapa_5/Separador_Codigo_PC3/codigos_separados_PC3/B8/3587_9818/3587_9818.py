from numpy import *
aneis = array(eval(input("insira: ")))
i = 0
ponto = 100.
while i < size(aneis):
	if aneis[i] == 1:
		ponto *= 5
	elif aneis[i] == 2:
		ponto *= 3
	elif aneis[i] == 3:
		ponto == ponto
	elif aneis[i] == 4:
		ponto /= 2
	i += 1
print(round(ponto, 2))
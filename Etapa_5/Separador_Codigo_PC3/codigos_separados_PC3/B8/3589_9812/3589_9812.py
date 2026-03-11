from numpy import *

aneis = array(eval(input("pontuacao: ")), dtype=int)

i = 0
total = 0

while i < size(aneis):
	if aneis[i] == 1:
		total += 80
	elif aneis[i] == 2:
		total += 40
	elif aneis[i] == 3:
		total += 20
	elif aneis[i] == 4:
		total += 10
	i += 1
print(total)
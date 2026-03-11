from numpy import* 

aneis = array(eval(input('quais foram  os acertos? ')))

i = 0
pts = 100.

while i < size(aneis):
	if aneis[i] == 1:
		pts *= 5
	elif aneis[i] == 2:
		pts *= 3
	elif aneis[i] == 4:
		pts /= 2
	i += 1
	
print(round(pts, 2))
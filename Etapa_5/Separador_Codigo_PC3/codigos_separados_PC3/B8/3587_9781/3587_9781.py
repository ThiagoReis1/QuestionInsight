from numpy import *

aneis = array(eval(input("quais os acertos?")))

i = 0
pt = 100.

while i < size(aneis):
	if aneis[i] == 1:
		pt *= 5
	elif aneis[i] == 2:
		pt *= 3
	elif aneis[i] == 4:
		pt /= 2
	i += 1
print(round(pt, 2))

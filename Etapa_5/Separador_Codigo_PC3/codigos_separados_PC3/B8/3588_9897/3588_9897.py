from numpy import *

aneis = array(eval(input('acertos: ')))

i = 0 #inidce
pnts = 10000

while i < size(aneis):
	if aneis[i] == 1:
		pnts *= 2
	elif aneis[i] == 3:
		pnts /= 2
	elif aneis[i] == 4:
		pnts /= 4
	i += 1
print(pnts)
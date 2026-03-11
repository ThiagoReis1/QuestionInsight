from numpy import *
pts = array(eval(input('anel acertado: ')))
i = 0
ponto = 100
while (i < size(pts)):
	if(pts[i] == 1):
		ponto = (ponto * 5)
	elif(pts[i] == 2):
		ponto = (ponto * 3)
	elif(pts[i] == 3):
		ponto = ponto
	elif(pts[i] == 4):
		ponto = (ponto / 2)
	i = i + 1
print(round(ponto, 2))
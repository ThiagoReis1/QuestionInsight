from numpy import *

dados = array(eval(input('quais foram as pontuacoes')))

i = 0
pts = 0

while i < size(dados):
	if dados[i] == 1:
		pts = pts + 10
	elif dados[i] == 2:
		pts = pts + 5
	elif dados[i] == 3:
		pts = pts + 0
	elif dados[i] == 4:
		pts = pts + 5
	elif dados[i] == 5:
		pts = pts + 20
	elif dados [i] == 6:
		pts = pts + 10
	i = i + 1
	
print(round(pts, 2))
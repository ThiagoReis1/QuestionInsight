from numpy import *
acertos = array(eval(input("valor acertado: ")))
pts = 100
i = 0

while i < size(acertos):
	if acertos[i] == 1:
		pts *= 5
	elif acertos[i] == 2:
		pts *= 3
	elif acertos[i] == 3:
		pts == pts
	elif acertos[i]==4:
		pts /=2
	
	i += 1
print(round(pts,2))
		
		
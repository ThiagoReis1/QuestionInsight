from numpy import *
tempo = array(eval(input("Tempo de chegada dos corredores: ")))
t=0
while t < size(tempo):
	if tempo[t]==min(tempo):
		print(t)
	t = t + 1
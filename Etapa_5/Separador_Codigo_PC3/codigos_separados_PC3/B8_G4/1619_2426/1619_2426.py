from numpy import *
t = array(eval(input("tempo: ")))
modo = array(eval(input("modo: ")))
i = 0
v = 0
while((i != size(t)) and (i != size(modo))):
	if(modo[i] == 'QUENTE'):
		v += t[i] * 90 * 0.005
	elif(modo[i] == 'MORNO'):
		v += t[i] * 45 * 0.005
	elif(modo[i] == 'FRIO'):
		v += t[i] * 0 * 0.005
	i = i + 1
print(round(v, 2))
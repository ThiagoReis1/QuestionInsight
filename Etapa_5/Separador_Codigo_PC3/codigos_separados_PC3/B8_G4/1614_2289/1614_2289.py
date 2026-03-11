from numpy import *
ali = array(eval(input()))
cal = array(eval(input()))

g0 = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
i = 0
while (i < size(ali)):
	if (ali[i] == "BANANA"):
		g0 = g0 + (cal[i]*0.97)
		i = i + 1
	elif (ali[i] == "BIFE"):
		g1 = g1 + (cal[i]*2.95)
		i = i + 1
	elif (ali[i] == "FEIJOADA"):
		g2 = g2 + (cal[i]*1.27)
		i = i + 1
	elif (ali[i] == "OMELETE"):
		g3 = g3 + (cal[i]*1.04)
		i = i + 1
	elif (ali[i] == "TOMATE"):
		g4 = g4 + (cal[i]*0.2)
		i = i + 1
print(round(g0 + g1 + g2 + g3 + g4, 2))
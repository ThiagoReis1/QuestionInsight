from numpy import*
t = array(eval(input("tempos de banho: ")))
m = array(eval(input("modos dos banhos: ")))
i = 0
p = 0.005
g = 0
while( i < size(t)):
	if(m[i] == "QUENTE"):
		g = g + t[i]*90
	elif(m[i] == "MORNO"):
		g = g + t[i]*45
	i = i + 1
valor = g*p
print(round(valor,2))
from numpy import*
t = array(eval(input("tempo:")))
m = array(input("MODO"))
i = 0
valor = 0.005

while (i < size(m) ):
	if(m[i] == "FRIO"):
		valor = t[i] * 0
	elif(m[i] == "MORNO"):
		valor = 45 * t[i] * valor
	elif(m[i] == "MORNO"):
		valor = 90 * t[i] * valor
print(valor)
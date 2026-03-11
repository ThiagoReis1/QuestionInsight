from numpy import *

a = array(eval(input("valor: ")))
g = array(eval(input("valor: ")))

i = 0  #contador
s = 0   #soma

while(i  < size(a)):
	if(a[i].upper() == "BANANA"):
		s = s + (0.97 * g[i])
		i = i + 1
	elif(a[i].upper() == "BIFE"):
		s = s + (2.95 * g[i])
		i = i + 1
	elif(a[i].upper() == "FEIJOADA"):
		s = s + (1.27 * g[i])
		i = i + 1
	elif(a[i].upper() == "OMELETE"):
		s = s + (1.04 * g[i])
		i = i + 1
	elif(a[i].upper() == "TOMATE"):
		s = s + (0.2 * g[i])
		i = i + 1

print(round(s, 2))
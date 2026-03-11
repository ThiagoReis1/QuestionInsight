from numpy import *

n = array(eval(input()))
m = array(eval(input()))

cont = 0
total = 0

while(cont < size(n)):
	if(n[cont] == "ALONGAMENTO"):
		total = total + 3 * m[cont]
	if(n[cont] == "CORRIDA"):
		total = total + 10.3 * m[cont]
	if(n[cont] == "ESCALADA"):
		total = total + 9.7 * m[cont]
	if(n[cont] == "DANCA"):
		total = total + 6.7 * m[cont]
	if(n[cont] == "HIDROGINASTICA"):
		total = total + 5 * m[cont]
	cont = cont + 1
print(round(total,2))
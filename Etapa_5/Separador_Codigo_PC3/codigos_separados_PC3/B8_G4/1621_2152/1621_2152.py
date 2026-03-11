from numpy import *
x = array(input("produtos: "))
y = array(eval(input("quantidades: ")))

i = 0

while(i<size(x)):
	if(x[i].upper() ==  "ARROZ"):
		A = y[i]*1.25
	elif(x[i].upper() ==  "FEIJAO"):
		F = y[i]*2.60
	elif(x[i].upper() ==  "BIS"):
		B = y[i]*1.80
	elif(x[i].upper() ==  "MIOJO"):
		M = y[i]*0.85
	elif(x[i].upper() ==  "FANTA"):
		T = y[i]*3.20
	i = i + 1
d = A+F+B+M+T
print(d)
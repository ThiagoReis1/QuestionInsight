from numpy import *
v1 = array(eval(input("Informe a atividade: ")))
v2 = array(eval(input("Informe o tempo da atividade: ")))
i = 0
a = 0
c = 0
d = 0
h = 0
e = 0
while(size(v1) > i):
	if(v1[i] == "ALONGAMENTO"):
		a = 3.0*v2[i]
	elif(v1[i] == "CORRIDA"):
		c = 10.3*v2[i]
	elif(v1[i] == "DANCA"):
		d = 6.7*v2[i]
	elif(v1[i] == "ESCALADA"):
		e = 9.7*v2[i]
	elif(v1[i] == "HIDROGINASTICA"):	
		h = 5.0*v2[i]
	i = i + 1	
print(round(a+c+d+e+h, 2))		
from numpy import *
vn = array(eval(input("Nomes de atividades fisicas: ")))
vt = array(eval(input("Duracao (em minutos) das atividades: ")))

n = 0
c = 0
while(n<size(vn)):
	if (vn[n]=="ALONGAMENTO"):
		c = c + 3*vt[n]
	elif (vn[n]=="CORRIDA"):
		c = c + 10.3*vt[n]
	elif (vn[n]=="DANCA"):
		c = c + 6.7*vt[n]
	elif (vn[n]=="ESCALADA"):
		c = c + 9.7*vt[n]
	elif (vn[n]=="HIDROGINASTICA"):
		c = c + 5*vt[n]
	n = n + 1
	
print(round(c, 2))
from numpy import *
n=array(eval(input("produto").upper()))
q=array(eval(int(input("preco"))))
i=0
dm=0

while(i<size (n)):
	if(n[i]=="ARROZ"):
		dm=dm+q[i]*1.25
	elif(n[i]=="FEIJAO"):
		dm=dm+q[i]*2.60
	elif(n[i]=="BIS"):
		dm=dm+q[i]*1.80
	elif(n[i]=="MIOJO"):
		dm=dm+q[i]*0.85
	elif(n[i]=="FANTA"):
		dm=dm+q[i]*3.20
	i=i+1
print(round(dm,2))

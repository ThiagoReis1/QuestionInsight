from numpy import*

v1=array(eval(input()))
v2=array(eval(input()))
cont=0
soma=0

while (cont < size(v1)):
	if(v1[cont]=="GELO"):
		soma=soma+(v2[cont]*2)
		cont=cont+1
	elif(v1[cont]=="FOGO"):
		soma=soma+(v2[cont]*3)
		cont=cont+1
	elif(v1[cont]=="CHOQUE"):
		soma=soma+(v2[cont]*4)
		cont=cont+1
	elif(v1[cont]=="CONJURACAO"):
		soma=soma+(v2[cont]*8)
		cont=cont+1
	elif(v1[cont]=="ILUSAO"):
		soma=soma+(v2[cont]*10)
		cont=cont+1
		
print(soma)
from numpy import*

n=array(eval(input("Numeros: ")))
m=0
i=0
#cont=0
soma=0
while(i<size(n)):
	#if(n[i]>0):
	soma=soma+((n[i])**(1/3))
	#cont=cont+1
	i=i+1

m=(soma/i)**3
print(round(m,2))

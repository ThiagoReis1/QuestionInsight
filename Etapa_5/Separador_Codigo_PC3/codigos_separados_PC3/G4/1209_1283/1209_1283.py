from numpy import*
r=array(eval(input("Digite aqui:")))
print(74.08)
i=0
cont=0
while(i<size(r)):
	if(r[i]>74.08):
		cont=cont+1
	i=i+1
print(cont)
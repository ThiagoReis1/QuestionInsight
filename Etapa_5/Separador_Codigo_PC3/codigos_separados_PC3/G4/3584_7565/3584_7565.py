from numpy import*
c=array(eval(input(": ")))
des=0.15
cont=0
for i in range(0,size(c)):
	if(c[i]>200):
		cont=cont+c[i]-(c[i]*des)
	else:
		cont=cont+c[i]
print(round(cont,2))
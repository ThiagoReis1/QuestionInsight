from numpy import *
anel=array(eval(input(" ")))
i=0
cont=0
while(i<size(anel)):
	if(anel[i]==1):
		cont=cont+80
	if(anel[i]==2):
		cont=cont+40
	if(anel[i]==3):
		cont=cont+20
	if(anel[i]==4):
		cont=cont+10
	i=i+1
print(cont)
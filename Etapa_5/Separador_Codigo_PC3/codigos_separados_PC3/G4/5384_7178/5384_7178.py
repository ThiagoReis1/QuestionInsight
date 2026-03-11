from numpy import *

pa=input("Digite uma palavra: ")
i=0
v=0

while (i<len(pa)):
	if(pa[i]=="A" or pa[i]=="E" or pa[i]=="I" or pa[i]=="O" or pa[i]=="U"):
		v=v+45.15
		i=i+1
	else:
		v=v+50.17
		i=i+1
print(round(v,2))
		
	
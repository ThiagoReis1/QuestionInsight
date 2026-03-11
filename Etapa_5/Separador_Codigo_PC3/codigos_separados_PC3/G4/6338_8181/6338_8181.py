from numpy import*
vt= array(eval(input(": ")))
ni = int(input(": "))
i = 0
cont = 0
while(i < size(vt)):
	if(vt[i]==ni):
		print(i)
	if(vt[i] > ni):
		cont=cont+1
	i=i+1
print(cont)
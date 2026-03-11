from numpy import*
n=array(eval(input("demandas: ")))


cont=0

for i in range(size(n)):
	if(n[i]>=n[0]):
		cont=cont+1	
	if(n[i]>=n[0] and i!=0):
		print(i)

print(cont-1)		
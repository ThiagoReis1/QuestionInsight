from numpy import*
v1= array(eval(input("escreva o vetor")))
i=0
cont=0

while(i<size(v1)):
	if(v1[i]==307):
		cont= cont + 1
		
	i = i + 1
else:
	print(307)
i=0
cont=0
while(i<size(v1)):
	if(v1[i]>307):  
		cont=cont+1
	i = i +1
print(cont)
	
		
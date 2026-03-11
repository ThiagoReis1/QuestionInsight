from numpy import*
v1= array(eval(input("escreva o vetor:")))
i=0
cont=0
while(i<size(v1)):
	if(v1[i] >=0):
		cont = cont + 1
	i = i + 1
	
v2= array(zeros(cont, dtype = float))
i = 0
cont = 0
while(i< size(v1)):
	if(v1[i] >=0):
		v2[cont] = v1[i]
		cont = cont + 1
	i = i + 1
print(v2)
		
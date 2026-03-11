from numpy import*

v1 = array(eval(input("escrever o valor do vetor: ")))
i =0 
cont = 0
t = 40
while (i<size(v1)):
	if(v1[i] > t):
	   cont = cont + 1
i = i + 1
	
v2= array(zeros(cont, dtype = float))
i=0
cont = 0 
t=40
while(i< size(v1)):
	if(v1[i] > t):
		v2[cont] = v1[i]
		cont = cont + 1
i= i + 1
print(v2)
		
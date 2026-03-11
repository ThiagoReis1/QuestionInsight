from numpy import* 

v= array(eval(input("Digite o vetor com o tempo de chegada dos corredores: ")))

i= 0

while(i < size(v)):
	if(v[i] == max(v)):
		v1= i
	i= i + 1
		
print(v1)
		
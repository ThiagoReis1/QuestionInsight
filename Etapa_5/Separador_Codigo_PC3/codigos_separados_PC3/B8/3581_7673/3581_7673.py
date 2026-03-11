from numpy import * 

vet = array(eval(input()))
i = 0
total = 0
while(i < size(vet)):
	if(vet[i] > 40):
	   total = total + vet[i] - 2.50
	elif(vet[i] <= 40):
		total = total + vet[i]
	i = i + 1
print(round(total, 2))
	
	





	

	

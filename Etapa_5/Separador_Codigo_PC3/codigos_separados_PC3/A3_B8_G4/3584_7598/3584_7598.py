from numpy import*

vet = array(eval(input()))
i = 0
des = 0
soma = 0


for i in range(size(vet)):
	if(vet[i] > 200):
		des = vet[i] * 15/100
		vet[i] = vet[i] - des
		
	elif(vet[i] < 200):
		vet[i] = vet[i]
		
print(round(sum(vet), 2))
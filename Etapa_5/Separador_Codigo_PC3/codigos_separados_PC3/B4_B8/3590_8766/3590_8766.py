from numpy import *   
vet = array(eval(input("Digite a face de dados:")))

i = 0
total = 0

while i < size(vet):
	if vet[i] == 1:
		total = total + 10
	elif vet[i] == 2:
		total = total +  5
	#elif vet[i] == 3:
		#total =  0
	elif vet[i] == 4:
		total = total +  5
	elif vet[i] == 5:
		total = total +  20
	elif vet[i] == 6:
		total = total +  10
	i = i + 1
	#total = total + 1
print(total)
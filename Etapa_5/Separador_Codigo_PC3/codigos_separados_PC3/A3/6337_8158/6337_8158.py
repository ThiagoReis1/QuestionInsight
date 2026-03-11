from numpy import *
vet = array(eval(input("Digite o vetor: ")))
num = int(input("Digite o numero: "))

i = 0 
acum1 = 0
acum2 = 0
x=0

while i < size(vet): 
	if vet[i] == num:
		print(i)
	if vet[i]<num:
		x = x + 1 
	i = i + 1 

print(x)
	

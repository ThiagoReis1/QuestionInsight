from numpy import *
vet = array(eval(input("Digites o sorotipos: ")))

tipos = zeros(4, dtype= int)
for i in range(size(vet)):
	if(vet[i] == 1):
		tipos[0] = tipos[0] + 1
	elif(vet[i] == 2):
		tipos[1] = tipos[1] + 1
	elif(vet[i] == 3):
		tipos[2] = tipos[2] + 1
	elif(vet[i] == 4):
		tipos[3] = tipos[3] + 1
print(tipos)
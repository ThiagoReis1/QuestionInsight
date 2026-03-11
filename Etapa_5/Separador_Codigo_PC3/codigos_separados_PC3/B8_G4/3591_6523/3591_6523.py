from numpy import*

vet = array(eval(input("Faces: ")))

i = 0
cont = 0
while(i < size(vet)):
	if(vet[i] == 1)or(vet[i] == 3)or(vet[i] == 5):
		cont = cont + 10
	elif(vet[i] == 2)or(vet[i] == 4)or(vet[i] == 6):
		cont = cont + 5
	i = i + 1
print(cont)
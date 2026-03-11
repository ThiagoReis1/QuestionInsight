from numpy import*
vet = input("Digite: ").split(',')
B = 0
PA = 0
PR = 0
A = 0
I = 0

for i in range(size(vet)):
	#print("ok")
	if(vet[i] == "B"):
		B += 1
	elif(vet[i] == "PA"):
		PA += 1
	elif(vet[i] == "PR"):
		PR += 1
	elif(vet[i] == "A"):
		A += 1
	elif(vet[i] == "I"):
		I += 1
qust = array([B,PA,PR,A,I])
print(max(qust))
print(qust)
		



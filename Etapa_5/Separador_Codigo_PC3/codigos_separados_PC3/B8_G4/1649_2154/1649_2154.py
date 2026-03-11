from numpy import*
from numpy.linalg import*

vet = input("cor dos olhos: ").split(',')

V = zeros(5,dtype=int)

for j in range(size(vet)):
	if(vet[j] == "P"):
		V[0] = V[0] + 1
	elif(vet[j] == "C"):
		V[1] = V[1] + 1
	elif(vet[j] == "M"):
		V[2] = V[2] + 1
	elif(vet[j] == "V"):
		V[3] = V[3] + 1
	elif(vet[j] == "A"):
		V[4] = V[4] + 1
print(int(max(V)))	
print(V)
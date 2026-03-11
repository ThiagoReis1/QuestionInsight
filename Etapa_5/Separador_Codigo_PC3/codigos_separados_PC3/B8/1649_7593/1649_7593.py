from nymp import * 

vet = array(eval(input("P"))).upper().split(',')

olhos = zeros(5, dtype=int)

for i in range(vet):
	if(vet[i] == "P"):
		olhos[0] = olhos[0] + 1
	elif(vet[i] == "C"):
		olhos[1]= olhos[1] + 1
	elif(vet[i] == "M"):
		olhos[2] = olhos[2] + 1
	elif(vet[i] == "V"):
		olhos[3] = olhos[3] + 1
	elif(vet[i] == "A"):
		olhos[4] = olhos[4] + 1
		

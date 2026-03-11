from numpy import*
st = input("STRING: ")
vet = zeros(5, dtype=int)
for i in st:
	if(i == "P"):
		vet[0] += 1
	elif(i == "C"):
		vet[1] += 1
	elif(i == "M"):
		vet[2] += 1
	elif(i == "V"):
		vet[3] += 1
	elif(i == "A"):
		vet[4] += 1
print(max(vet))
print(vet)
	
		

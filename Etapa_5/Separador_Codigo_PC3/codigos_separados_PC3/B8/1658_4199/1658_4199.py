from numpy import*
stringp = input(" ")
vet =zeros(5,dtype = int)
for i in stringp.split(','):
	if(i =="CHN"):
		vet[0] = vet[0] + 1
	elif(i == "JPN"):
		vet[1] = vet[1] + 1
	elif(i == "KOR"):
		vet[2] = vet[2] + 1
	elif(i == "MGL"):
		vet[3] = vet[3] + 1
	elif(i == "THA"):
		vet[4] = vet[4] + 1
print(max(vet))
print(vet)
	
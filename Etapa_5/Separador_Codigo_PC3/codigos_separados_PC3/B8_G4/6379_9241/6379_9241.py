from numpy import*
a= input("digite a nota:").upper()
cont= zeros(5, dtype=int)

for i in range(len(a)):
	if(a[i] == "A"):
		cont[0] += 1
	elif(a[i] == "B"):
		cont[1] += 1
	elif(a[i] == "C"):
		cont[2] += 1
	elif(a[i] == "D"):
		cont[3] += 1
	elif(a[i] == "E"):
		cont[4] += 1
print(cont)
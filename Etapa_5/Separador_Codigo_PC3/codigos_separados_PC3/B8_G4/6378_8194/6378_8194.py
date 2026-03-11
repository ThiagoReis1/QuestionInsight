from numpy import*

n = input("Digite: ").upper().split(",")
cont = zeros(4,dtype=int)

for i in range(size(n)):
	if(n[i] == "C"):
		cont[0] = cont[0] + 1
	elif(n[i] == "D"):
		cont[1] = cont[1] + 1
	elif(n[i] == "V"):
		cont[2] = cont[2] + 1
	elif(n[i] == "U"):
		cont[3] = cont[3] + 1
print(cont)
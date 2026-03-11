var = input(""). upper()
H = 0
C = 0
L = 0
cont = 0
i = 0
while(i< len(var)):
	if(var[i]== "H"):
		H = H + 1
		cont = cont + 5.40
	elif(var[i] == "C"):
		C = C + 1
		cont = cont + 8.95
		
	elif(var[i] == "L"):
		L = L + 1
		cont = cont + 4.50
	i = i + 1
print(round(cont , 2) , H , C , L)		
	
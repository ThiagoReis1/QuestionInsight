cor= str(input()).upper( )
cont= 0
while cor != "S" :
		if cor == "VERMELHA":
			cont= cont + 1
			cor= str(input()).upper()
print(cont)
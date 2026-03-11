x = input("voce gostou?: ").upper()
cont = 0
while (x != "S"):
	if(x == "SIM"):
		cont = cont + 1
		x = input("voce gostou?: ").upper()
	else:
		x = input("voce gostou?: ").upper()
print(cont)
		
	


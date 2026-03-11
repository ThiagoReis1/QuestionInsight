constSIM = 0 
while(True):
	va1 = input("imput de satisfacao: ")
	va1= va1.upper()
	if(va1 == "S"):
		break 
	if(va1 == "SIM"):
		constSIM = constSIM + 1
print(constSIM)
x = "V"



cont = 0

while x != "S":
	x = input("Digite a cor da casa:").upper()
	
	if x == "PRETA":
		cont += 1 
		
print(cont)
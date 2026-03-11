confronto = input()
cont = 0

while confronto.upper() != "X":
	if confronto.upper() == "A":
		cont = cont + 1
		
	confronto = input()
	
print(cont)
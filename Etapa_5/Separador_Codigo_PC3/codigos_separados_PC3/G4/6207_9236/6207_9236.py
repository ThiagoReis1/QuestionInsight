nmr = int(input("Digite o numero:"))
cont = 0
while (nmr != -1):
	if (26 <= nmr <= 50):
		cont = cont + 1
	nmr = int(input("Digite o numero:"))
	
print(cont)
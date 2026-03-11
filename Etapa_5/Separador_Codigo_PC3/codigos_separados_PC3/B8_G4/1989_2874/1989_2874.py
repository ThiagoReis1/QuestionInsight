#Le as entradas:
amino = input("Aminoacido:").upper()
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794

#Algoritmo:
if(amino == "ASPARAGINA" or amino == "GLUTAMINA" or amino == "TRIPTOFANO"):
	if(amino == "ASPARAGINA"):
		peso = 4 * c + 8 * h + 2 * n + 3 * o 
		print(round(peso,2))
	elif(amino == "GLUTAMINA"):
		peso = 5 * c + 8 * h + 1 * n + 4 * o 
		print(round(peso,2))
	elif(amino == "TRIPTOFANO"):
		peso = 11 * c + 11 * h + 2 * n + 2 * o 
		print(round(peso,2))
		
	
else:
	print("Entrada:",amino)
	print("Dado Invalido")
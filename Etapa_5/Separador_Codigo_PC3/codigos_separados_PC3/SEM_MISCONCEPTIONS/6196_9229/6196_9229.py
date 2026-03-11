altura = float(input(" "))
taxa = float(input(" "))
altura_chico = 1.5
taxa_chico = 0.02

anos = 0 

while altura < altura_chico:
	altura = altura + taxa
	altura_chico = altura_chico + taxa_chico
	anos = anos + 1
print(anos)
	
	
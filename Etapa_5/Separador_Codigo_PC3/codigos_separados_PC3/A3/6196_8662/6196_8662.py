altura = float(input('Digite o valor: ')) 
taxa = float(input('Digite o valor: '))
altura_chico = 1.5
taxa_chico = 0.02
anos = 0

while altura < altura_chico:
	altura_chico = altura_chico + 0.02
	altura = altura + taxa
	anos = anos + 1

print(anos)
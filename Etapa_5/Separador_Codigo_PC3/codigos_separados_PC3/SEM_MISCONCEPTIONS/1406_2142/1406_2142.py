tipo_de_ataque = input("Digite o tipo de ataque: ")
valor = int(input("Digite o valor sorteado: "))
numero_de_turnos= int(input("Digite o numero de turnos: "))

if(tipo_de_ataque == "cauda"):
	x = valor * numero_de_turnos
	
else:
	x = (2 * valor) * numero_de_turnos
	
print(x)
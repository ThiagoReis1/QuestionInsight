ataque = input("Tipo de ataque:")
dado = int(input("Valor sorteado no dado:"))
turnos = int(input("Numero de turnos:"))

if(ataque):
	num= dado * turnos
	print(num)
	
else:
	num= 2 * dado * turnos
	print(num)
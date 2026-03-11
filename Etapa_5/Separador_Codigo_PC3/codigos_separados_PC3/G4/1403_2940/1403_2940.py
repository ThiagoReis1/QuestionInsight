## entradas
arm = input('Informe o nome da armadura (malha/placas): ')
fat = int(input('Informe o faor de destreza (1-8): '))

if(arm == "malha"):
	res = (15 * fat) - 1
else:
	res = (20 * fat) - 18
print(res)
	
	


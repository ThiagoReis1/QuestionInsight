nome = input("Insira o nome da armadura:")
destreza = int(input("Insira o valor do dado:"))

if(nome.lower() == 'malha'):
	resistencia = (15*destreza) -1
	print(resistencia)
	
if(nome.lower() == 'placas'):
	resistencia = (20*destreza) - 18
	print(resistencia)

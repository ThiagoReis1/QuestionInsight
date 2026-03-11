#Variaveis

nome_1 = "Aamel"
nome_2 = "Hethradiah"

ataque = input("Nome da cabeca")

dado_1 = int(input("Valor dado 1"))

dado_2 = int(input("Valor dado 2"))

dado_3 = int(input("Valor dado 3"))

if (ataque == "Aamel"):
	dano_fixo = 8
	dano_ale = (dado_1 + dado_2 + dado_3)
	
	ataque_final = (dano_fixo + dano_ale)
	
	print(ataque_final)
	
else:
	ataque_final = 2 * (dado_1 + dado_2 + dado_3)
	
	print(ataque_final)
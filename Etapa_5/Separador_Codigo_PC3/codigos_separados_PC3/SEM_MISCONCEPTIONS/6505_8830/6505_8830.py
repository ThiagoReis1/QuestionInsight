# faça seu código aqui!
combo = 30
escolha = input("A/B/C? ")
quantidade= int(input("quantidade de combos desejada: "))
 

if escolha.upper() == "C":
	conta = (combo * quantidade)-((combo*quantidade)*0.15)
	print(round(conta,2))
else:
	conta = combo * quantidade
	print(round(conta,2))
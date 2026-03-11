opcao = input("torta ou pastel? T/P ")
quantidade_tortapastel = int(input(" "))
quantidade_cappuccinos = int(input(" "))

if opcao == "T":
	precofinal = (quantidade_cappuccinos*4.5)+(quantidade_tortapastel*6)
	print(round(precofinal, 1))
	
else:
	precofinal = (quantidade_cappuccinos*4.5)+(quantidade_tortapastel*5)
	print(round(precofinal, 1))
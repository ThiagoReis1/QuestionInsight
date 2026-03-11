opcao = input("[B] Bolo\n[C] Croissant\nEscolha: ").upper()
fatias_bolo = 0
croissants = 0

if (opcao == "B"):
	fatias_bolo = int(input(""))
else:
	croissants = int(input(""))
	
cappuccinos = int(input(""))

total = (fatias_bolo * 3) + (croissants * 6) + (cappuccinos * 5.5)

print(round(total, 1))
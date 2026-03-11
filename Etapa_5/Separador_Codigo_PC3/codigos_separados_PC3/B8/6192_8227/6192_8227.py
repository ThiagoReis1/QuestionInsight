contador_pretas = 0
	
while True:
		cor_da_casa = input("digite cor da casa:")
		if cor_da_casa == "PRETA":
			contador_pretas += 1
		elif cor_da_casa == "S":
			break
print(contador_pretas)			
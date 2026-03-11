hora = float(input("Inserir valor do tempo: "))

subtotal= hora * 15 + 5
	
icms= .20

#total = 100% + 20%

total = (subtotal * 1.0) + (subtotal * icms)

print(round(total, 2))
peso = float(input("Peso da encomenda: "))

tarifa = 0
taxa = 0

if peso >=0 and peso <= 5000:
		tarifa = 0.03
		taxa = 20.
if peso >= 5001 and peso <= 6000:
		tarifa = 0.04
		taxa = 25.
if peso >= 6001 and peso <= 7000:
		tarifa = 0.05
		taxa = 30.
if peso > 7000:
		tarifa = 0.06
		taxa = 35.
valor = peso*tarifa+taxa		
print(round(valor, 2))		
	
		
		


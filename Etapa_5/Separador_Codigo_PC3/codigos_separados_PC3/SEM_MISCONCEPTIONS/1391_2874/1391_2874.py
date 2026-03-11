#Lê o o valor da energia consumida em kwh:

energia = float(input("Consumo mensal de energia:"))

# Calcula a tarifa:

if(energia <= 150.0):
	tarifa = 5 + 0.6 * energia
	
else:
	tarifa = 16 + 0.75 * energia
	
conta = round(tarifa,2)
print(conta)
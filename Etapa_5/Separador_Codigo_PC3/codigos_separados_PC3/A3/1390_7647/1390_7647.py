consumo = float(input("Insira o Consumo de Minutos: "))

if(consumo <= 100):
	valor_da_conta = 1.20 * consumo

if(consumo > 100):
	valor_da_conta = 25 + (1.4 * consumo)
	
print(round(valor_da_conta,2))
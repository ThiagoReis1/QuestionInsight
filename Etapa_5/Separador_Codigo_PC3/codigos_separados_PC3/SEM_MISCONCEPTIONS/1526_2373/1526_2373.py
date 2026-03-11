quant_inicial = int(input("Quant. Inicial de Mana: "))
quant_gasta = int(input("Gasto Diario: "))
quant_recupera = int(input("Quant. mana: "))
dias = 0
energia = quant_inicial
while(energia > 0):
	dias = dias + 1
	energia = energia - quant_gasta + quant_recupera
	
print(dias)
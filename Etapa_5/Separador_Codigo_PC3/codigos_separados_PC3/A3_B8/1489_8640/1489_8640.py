rf = int(input("digite o valor da conta de energia:"))
valor = 0
if (rf >= 0 and rf <= 150):
	 valor = rf * 0.60 + 5
elif (rf >= 150 and rf <= 250):
	valor = rf * 0.65 + 8
elif (rf >= 250 and rf <= 350):
	valor =  rf * 0.70 + 12
elif (rf > 350):
	valor = rf * 0.75 + 16

print(valor)
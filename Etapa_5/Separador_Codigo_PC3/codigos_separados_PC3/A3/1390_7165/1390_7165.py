consumo = float(input("consumo de minutos :"))
taxa = 25

if(consumo <= 100):
	tarifa = round(consumo*1.20, 2)
else:
	tarifa = round(25 + consumo*1.4 , 2)
print(tarifa)
	
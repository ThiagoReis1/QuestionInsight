consumo=int(input("digite o consumo em minutos:"))

if(consumo<=100):
	tarifa=consumo*(1.20)
	print(tarifa)
if(consumo>100):
	tarifa= consumo*1.40 +25
	print(float(tarifa))
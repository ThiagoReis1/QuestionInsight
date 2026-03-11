consumo = float(input("qual o consumo: "))

if(consumo>100):
	m = 25.00 + (consumo*1.40)
else:
	m = (consumo*1.20)
print(round(m,2))
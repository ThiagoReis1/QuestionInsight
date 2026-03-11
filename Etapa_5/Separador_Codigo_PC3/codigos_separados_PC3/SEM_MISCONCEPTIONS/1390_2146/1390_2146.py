consumo = float(input("Consumo: "))
x = (consumo * 1.20)
y = (consumo * 1.40)

if(consumo <= 100):
	print(round(x, 2))
if(consumo > 100):
	print(round(y + 25, 2))
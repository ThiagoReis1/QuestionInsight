area = float(input("Informe a area: "))

if(0<=area<=100):
	valor = area * 2 + 100
	print(round(valor,2))
elif(100<area<=2500):
	valor = area * 1.8 + 150
	print(round(valor,2))
elif(2500<area<=10000):
	valor = area * 1.5+ 200
	print(round(valor,2))
elif(10000<area):
	valor = area * 1.2+ 250
	print(round(valor,2))

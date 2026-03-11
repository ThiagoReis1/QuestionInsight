entrada = input("aminoacido: ").lower()
o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079
histidina = (c * 6) + (h * 10) + (n * 3) + (o * 2)
leucina = (c * 6) + (h * 13) + (n) + (o * 2)
lisina = (c* 6) + (h * 15) + (n * 2)  + (0 * 2)

if(entrada == "histidina"):
	print(round(histidina, 2))
elif(entrada == "leucina"):
	print(round(leucina, 2))
elif(entrada == "lisina"):
	print(round(lisina, 2))
else:
	print("Entrada:", h)
	print("Dado invalido")
	
						
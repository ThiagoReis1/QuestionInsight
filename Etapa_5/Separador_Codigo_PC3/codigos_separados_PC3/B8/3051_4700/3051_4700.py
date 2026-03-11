consumo = float(input("Digite o consumo: "))

if (0 <= consumo <= 150):
	valor = (consumo*0.6+5)
elif(150 < consumo <= 250):
	valor = (consumo*0.65+8)
elif(250 < consumo <= 350):
	valor = (consumo*0.7+12)
elif(consumo>350):
	valor = (consumo*0.75+16)

print(round(valor,2))
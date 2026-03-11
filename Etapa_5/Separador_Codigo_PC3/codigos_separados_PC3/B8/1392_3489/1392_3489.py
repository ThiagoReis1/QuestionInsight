con = float(input("insira o consumo: "))

if (0 < con < 10) :
	calculo = 30 + con * 3
elif (0 < con >= 10) :
	calculo = 30 + con * 3.5
	
print(round(calculo,2))
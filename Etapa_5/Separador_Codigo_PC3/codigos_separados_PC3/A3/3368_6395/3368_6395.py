#temperatura da escala Celsius(C) para Kelivn
escala = input("Digite a escala em que a Temperatura C ou K: ")
v_temperatura = float(input("Digite o valor da temperatura: "))

if(v_temperatura):
	C = K - 273.15
	K = C + 273.15
else:
   print(round(v_temperatura, 2))
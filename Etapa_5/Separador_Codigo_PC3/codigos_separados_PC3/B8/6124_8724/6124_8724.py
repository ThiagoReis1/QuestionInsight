a = float(input("peso do tripulante: "))

if (3000.0<=a<3400.0):
	calculo =  a*0.8
	print(calculo)
elif (3400.0<= a <3900):
	calculo = a*1.3
	print(calculo)
elif (3900 <= a < 4100):
	calculo = a*2.1
	print( calculo)
elif (a>4100.0):
	calculo = a*3.0
	print(calculo)
	
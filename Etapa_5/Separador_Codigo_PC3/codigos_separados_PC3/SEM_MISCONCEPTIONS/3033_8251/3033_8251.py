x = float(input("insira um numero: "))

if(-100 < x < 0):
	resultado = -(1/x)
	print(round(resultado, 4))
	
elif( 0< x <= 100):
	resultado = 1/x
	print(round(resultado, 4))

else: 
	print("entrada invalida")
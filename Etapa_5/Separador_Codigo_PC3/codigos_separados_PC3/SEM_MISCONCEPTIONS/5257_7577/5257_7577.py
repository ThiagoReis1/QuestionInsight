var = float(input(": "))

if(50 <= var):
	valor = var + 1
   elif(50 <= var or 100 <= var):
	valor = var + 0.5
   elif(var > 100):
	valor = var + 0.3
else:
	valor = 500 + 0.3
	print(round(valor, 2))
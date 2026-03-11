x = float(input("valor consumido no restaurante: "))

if(x <= 300.0):
	valor_total = x + 10/100 * x
else:
	valor_total = x + 6/100 * x
   
print(round(valor_total, 2))
	
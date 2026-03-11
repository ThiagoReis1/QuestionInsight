volume = float(input(""))
valor = 0

if volume >= 0.0 and volume <= 10.0:
	valor = volume*3.00 + 15.00
	
	
elif volume >= 10.0 and volume <= 15.0:
	valor = volume*3.50 + 20.00
	

elif volume >= 15.0 and volume <= 20.00:
	valor = volume*4.00 + 25.00
		
else:
	valor = volume*4.50 + 30.00
	
print(round(valor, 2))
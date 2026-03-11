peso = float(input(":"))

if peso < 5000:
	
	total = peso * 0.05
	
	print(round(total,2))
	
else:
	
	total = (peso * 0.04) + 60
	
	print(round(total,2))

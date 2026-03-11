h = int(input("informe as horas: "))

dp = (h - 20)

if (h <= 20):
	c = h*50
	
else:
	c = (h*50) - (dp*50) + (dp*70) 
	
print(round(c, 2))


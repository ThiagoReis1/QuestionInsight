v = float(input("valor consumido no restaurante: "))

if v <= 300:
	j = v * 0.10 + v
	print(round(j,2))
	
else:
	j = v*0.06 + v
	print(round(j,2))
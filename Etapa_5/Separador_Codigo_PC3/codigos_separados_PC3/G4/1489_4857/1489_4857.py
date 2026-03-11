v = float(input("Digite o consumo de energia: "))

if (v>0) and (v<150):
	c = (v*0.6)+5
	print(round(c,2))
elif (v > 150) and (v < 250):
	c = (v*0.65)+8
	print(round(c,2))
elif (v > 250) and (v < 350):
	c = (v*0.70) +12
	print(round(c,2))
else:
	c = (v*0.75) + 16
	print(round(c,2))
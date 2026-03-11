energia=float(input("Digite o consumo de energia: "))

if(energia<=150):
	var=(0.60*energia)+5
	print(round(var,2))
else:
	var=(0.75*energia)+16
	print(round(var,2))
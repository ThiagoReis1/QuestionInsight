# faça seu código aqui!
dia = int(input("dia:"))

if dia < 15:
	total = 175*dia +20
	print(round(total,2))
	
elif dia == 15:
	total = dia*175 + 16
	print(round(total,2))
	
else:
	total = 175*dia + 10
	print(round(total,2))
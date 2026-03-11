sq = input("seg / qua: ")
p = int(input("insira a qtde de pratos: "))

if (sq == "qua"):
	total = p * 22 - (p * 22) * 0.15
	print(round(total, 2))
	
else: 
	total = p * 22
	print(round(total, 2))
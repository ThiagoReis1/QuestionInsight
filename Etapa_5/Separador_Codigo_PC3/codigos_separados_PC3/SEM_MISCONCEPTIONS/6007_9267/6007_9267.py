nespigas = float (input("Digite a quantidade de espigas: "))
if(nespigas < 7):
	total = nespigas * 1.85
else:
	total = nespigas * 1.50
print(round(total,2))
custof = 50
dist = int(input("Digite a distancia:"))

if dist < 10:
	taxa = 5.50
	
elif dist == 10:
	taxa = 7.75
	
else:
	taxa = 10
	
print(custof+taxa)
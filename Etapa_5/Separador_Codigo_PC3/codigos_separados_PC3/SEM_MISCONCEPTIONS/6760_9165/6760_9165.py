pecas = int(input("Quantidade de pecas de roupa para lavagem: "))
				
if (pecas < 10):
	taxa = 3.25
elif (pecas == 10):
	taxa = 4.50
else:
	taxa = 6.0
				
total = 30 + taxa
				
print(round(total, 2))				
x = int(input("Digite a quantia da compra: "))

if x >= 3: 
	total = x * 4.25
else: 
	total = x * 5
	
print(round(total,2))
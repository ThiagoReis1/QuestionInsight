from numpy import*

product = input("Produtos: ").upper()

i = 0
contA = 0
contL = 0
contP = 0
total = 0

while i < len(product):
	if product[i] == 	"A":
		total = total + 19.90
		contA = contA + 1
		i = i + 1
	elif product[i] == "L":
		total = total + 3.50
		contL = contL + 1
		i = i + 1
	elif product[i] == "P":
		total = total + 4.25
		contP = contP + 1
		i = i + 1
		
print(round(total,2), contA, contL, contP)
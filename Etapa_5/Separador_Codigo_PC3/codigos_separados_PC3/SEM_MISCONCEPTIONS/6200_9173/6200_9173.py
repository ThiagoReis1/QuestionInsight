altura_max = 1.75
taxa_max = 0.01
altura = float(input())
taxa = float(input())
anos = 0

while altura_max > altura:
	altura = altura + taxa
	altura_max = altura_max + taxa_max
	anos += 1
	
print(anos)
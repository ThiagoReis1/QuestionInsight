alt_max = 1.75
taxa_max = 0.01
cont = 0

alt = float(input())
taxa = float(input())

while alt < alt_max:
	alt_max = alt_max + taxa_max
	alt = alt + taxa
	cont += 1
	
print(cont)
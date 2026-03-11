altura_luna = 1.65
taxa_luna = 0.02
alt = float(input())
taxa = float(input())
anos = 0

while alt < altura_luna:
	altura_luna = altura_luna + taxa_luna
	alt = alt + taxa
	anos = anos + 1
print(anos)
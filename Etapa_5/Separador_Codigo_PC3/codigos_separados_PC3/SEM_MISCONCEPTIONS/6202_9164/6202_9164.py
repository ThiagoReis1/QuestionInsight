altura_bia = 1.69
taxa_bia = 0.01

alt = float(input())
taxa = float(input())

anos = 0

while altura_bia > alt:
	alt = alt + taxa
	altura_bia = altura_bia + taxa_bia
	anos = anos + 1

print(anos)
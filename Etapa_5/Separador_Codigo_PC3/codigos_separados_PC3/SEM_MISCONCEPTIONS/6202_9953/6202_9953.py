alt = float(input())
taxa = float(input())
altura_bia = 1.69
taxa_bia = 0.01
anos = 0
while alt <= altura_bia:
	alt = alt + taxa
	altura_bia = altura_bia + taxa_bia
	anos += 1
print(anos)
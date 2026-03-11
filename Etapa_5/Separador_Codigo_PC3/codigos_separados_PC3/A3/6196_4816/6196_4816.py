altura_chico = 1.5
taxa_chico = 0.02

alt = float(input())
taxa = float(input())

anos = 0


while alt < altura_chico:
	alt = alt + (1+taxa)
	altura_chico = altura_chico + (1.02)
	anos += 1
	
print(anos)
	
altura_chico = 1.5
taxa_chico = 0.02
altura = float(input())
taxa = float(input())

anos = 0 

while altura < altura_chico:
	altura_chico += taxa_chico
	altura += taxa
	anos += 1
	
print(anos)
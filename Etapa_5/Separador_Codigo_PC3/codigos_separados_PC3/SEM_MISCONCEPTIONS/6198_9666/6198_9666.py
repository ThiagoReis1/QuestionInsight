altura_luna = 1.65
taxa_luna = 0.02

altura = float(input())
taxa = float(input())

tempo = 0

while altura < altura_luna:
	altura += taxa
	altura_luna += taxa_luna
	tempo += 1
	
print(tempo)
	
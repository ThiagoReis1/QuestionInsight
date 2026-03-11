altura_cicero = 1.8
taxa_cicero = 0.01

alt = float(input())
tax = float(input())

tempo = 0

while alt <= altura_cicero:
	altura_cicero += taxa_cicero
	alt += tax
	tempo +=1
print(tempo)
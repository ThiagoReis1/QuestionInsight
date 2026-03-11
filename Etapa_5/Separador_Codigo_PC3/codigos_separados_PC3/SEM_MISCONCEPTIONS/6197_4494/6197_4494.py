altura_alice = 1.6
taxa_alice = 0.02

altura = float(input())
taxa = float(input())

cont = 0

while altura < altura_alice:
	altura += taxa
	altura_alice += taxa_alice
	cont += 1

print(cont)
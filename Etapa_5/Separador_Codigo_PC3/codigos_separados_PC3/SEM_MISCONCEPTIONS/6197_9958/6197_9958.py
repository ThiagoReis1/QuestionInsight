altura_alice = 1.6
taxa_alice = 0.02

altura = float(input("altura"))
taxa = float(input("taxa"))
cont = 0

while altura < altura_alice:
	altura_alice = altura_alice + taxa_alice
	altura = altura + taxa
	cont = cont +1
print(cont)

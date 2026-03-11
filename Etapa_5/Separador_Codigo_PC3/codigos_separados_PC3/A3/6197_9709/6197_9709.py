altura_alice = 1.6
taxa_alice = 0.02

taxa_crescimento_alice = 0.01

altura_pessoa = float(input())
taxa_pessoa = float(input())

anos = 0

while altura_pessoa < altura_alice:
	
	altura_alice += taxa_alice
	altura_pessoa += taxa_pessoa
	anos += 1
	
print(anos)

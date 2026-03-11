altura_alice = 1.6
taxa_alice = 0.02
altura_pessoa = float(input("digite altura:"))
taxa_pessoa = float(input("digite crescimento:"))
ano = 0

while altura_pessoa < altura_alice:
	
	altura_alice = altura_alice + taxa_alice
	altura_pessoa = altura_pessoa + taxa_pessoa
	ano += 1
	
print(ano)

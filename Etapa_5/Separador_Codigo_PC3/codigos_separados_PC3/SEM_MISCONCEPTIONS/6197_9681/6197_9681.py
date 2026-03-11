altura_alice = 1.6
taxa_alice = 0.02
alt_aluno = float(input("Altura: "))
taxa = float(input("Taxa de crescimento: "))
anos = 0
while altura_alice + taxa_alice >= alt_aluno + taxa:
	alt_aluno = alt_aluno + taxa 
	altura_alice = altura_alice + taxa_alice 
	anos = anos + 1
print(anos)
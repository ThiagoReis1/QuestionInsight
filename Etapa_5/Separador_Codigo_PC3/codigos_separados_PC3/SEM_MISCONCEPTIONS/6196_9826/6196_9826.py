alt_chico = 1.5
taxa_chico = 0.02
alt_pessoa = float(input("insira uma altura: "))
taxa_pessoa = float(input("insira a taxa: "))
ano = 0

while alt_pessoa < alt_chico:
		alt_chico += taxa_chico
		alt_pessoa += taxa_pessoa
		ano += 1
print(ano)
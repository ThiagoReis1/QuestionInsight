altura_alice = 1.6
taxa_alice = 0.02

altura_pessoa = float(input("informe uma altura: "))
taxa_pessoa = float(input("informe a taxa de crescimento de uma pessoa: "))

anos = 0

while(altura_pessoa <= altura_alice):
	if(taxa_pessoa <= taxa_alice):
		anos = anos + 1
	else:
		print(anos)
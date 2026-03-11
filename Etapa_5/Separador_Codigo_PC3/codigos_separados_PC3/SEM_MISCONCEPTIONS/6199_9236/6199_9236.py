altura_pessoa = float(input("Digite a altura da pessoa:"))
taxa = float(input("Digite a taxa de crescimento: "))

altura_cicero = 1.8
taxa_cicero = 0.01
anos = 0

while(altura_pessoa <= altura_cicero):
	altura_pessoa = altura_pessoa + taxa
	altura_cicero = altura_cicero + taxa_cicero
	anos = anos + 1
	
print(anos)
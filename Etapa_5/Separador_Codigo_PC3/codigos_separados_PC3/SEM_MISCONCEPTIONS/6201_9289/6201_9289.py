altura_joe = 1.77
taxa_joe = 0.02

altura_atual = float(input("Digite a altura atual da pessoa: "))
taxa_crescimento = float(input("Digite a taxa de crescimento: "))
anos = 0

while altura_joe > altura_atual :
	altura_atual = altura_atual + taxa_crescimento
	altura_joe = altura_joe + taxa_joe
	anos = anos + 1
	
print(anos) 
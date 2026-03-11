altura = float(input("Digite a altura: "))
taxa = float(input("Digite a taxa: "))

altura_macaco = 1.40
taxa_macaco = 0.06
anos = 0

while altura > altura_macaco:
	altura = altura + taxa
	altura_macaco = altura_macaco + taxa_macaco
	anos = anos + 1
print(anos)
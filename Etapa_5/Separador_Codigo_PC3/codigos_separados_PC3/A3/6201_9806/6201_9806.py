altura_joe = 1.77
taxa_joe = 0.02
alt_pessoa= float(input("Altura: "))
taxa_pessoa = float(input("taxa de crescimento: "))
anos = 0
#while alt_pessoa <= altura_joe:
while altura_joe > alt_pessoa:
	alt_pessoa = alt_pessoa + taxa_pessoa
	altura_joe= altura_joe + 0.02
	anos = anos + 1
print(anos)
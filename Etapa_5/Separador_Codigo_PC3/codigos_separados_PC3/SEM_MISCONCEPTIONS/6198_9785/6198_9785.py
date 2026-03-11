altura_luna = 1.65
taxa_crescimento_luna = 0.02

altura_pessoa = float(input())
taxa_crescimento_pessoa = float(input())

anos = 0

while altura_pessoa <= altura_luna:
	altura_pessoa += taxa_crescimento_pessoa
	altura_luna+= taxa_crescimento_luna
	anos += 1
	
print(anos)
	
altura = float(input(""))
taxa = float(input(""))

ano = 0

altura_macaco = 1.4
taxa_macaco = 0.06

while altura > altura_macaco:
	altura = altura + taxa
	altura_macaco = altura_macaco + taxa_macaco
	ano = ano + 1
	
print(ano)
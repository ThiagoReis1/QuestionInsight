altura_macaco = 1.4
taxa_macaco = 0.06

altura_leao = float(input("digite a altura:"))
crescimento_leao = float(input("digite a altura:"))

anos = 0

while altura_leao >= altura_macaco:
	altura_macaco = altura_macaco + taxa_macaco
	altura_leao = altura_leao + crescimento_leao
	anos += 1
	
print(anos)
leao = float(input("digite a altura:"))
taxa_crescimento = float(input("digite a taxa:"))
altura_macaco = 1.4
taxa_macaco = 0.06
conta = 0 
while (leao > altura_macaco):
	leao = leao + taxa_crescimento
	altura_macaco = altura_macaco + taxa_macaco
	conta = conta + 1
print(conta)
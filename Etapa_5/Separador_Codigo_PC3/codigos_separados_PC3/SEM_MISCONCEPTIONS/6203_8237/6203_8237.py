altura_macaco = 1.4
taxa_macaco = 0.06

altura_leao = float(input("Digite um valor:"))
taxa_leao = float(input("Digite um valor:"))
cont = 0 

while altura_macaco < altura_leao:
	altura_macaco = altura_macaco + taxa_macaco
	altura_leao = altura_leao + taxa_leao
	cont = cont + 1
	
print(cont)
	
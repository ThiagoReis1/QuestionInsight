altura_macaco = 1.4
taxa_macaco = 0.06

altura_leao = float(input("Altura do leao: "))
taxa_leao = float(input("Altura leao: "))

cont = 1

macaco = altura_macaco + taxa_macaco
leao = altura_leao +  taxa_leao

while macaco <= leao:
	macaco = macaco + taxa_macaco
	leao = leao + taxa_leao
	cont = cont + 1
print(cont)
	


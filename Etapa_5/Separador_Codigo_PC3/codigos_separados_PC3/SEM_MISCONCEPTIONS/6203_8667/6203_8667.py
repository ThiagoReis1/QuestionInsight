altura_macaco = 1.4
taxa_macaco = 0.06
cont = 0

altura_leao = float(input("Digite a altura do leao: "))
taxa_leao = float(input("Digite a taxa de crescimento leao: "))

while(altura_macaco < altura_leao):
	altura_macaco = altura_macaco + taxa_macaco
	altura_leao = altura_leao + taxa_leao
	cont = cont + 1
	
print(cont)
	

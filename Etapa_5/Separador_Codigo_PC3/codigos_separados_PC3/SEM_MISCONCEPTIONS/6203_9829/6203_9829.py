altura_macaco = 1.4
taxa_macaco = 0.06

altura_leao = float(input("Insira a altura do leao: "))
taxa_leao = float(input("Insira a taxa de crescimento do leao: "))
ano = 0
while altura_macaco <= altura_leao:
	altura_leao += taxa_leao
	altura_macaco += taxa_macaco
	ano +=1
print(ano)
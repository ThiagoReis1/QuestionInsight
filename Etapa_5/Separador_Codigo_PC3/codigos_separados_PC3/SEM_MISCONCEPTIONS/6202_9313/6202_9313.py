altura_bia = 1.69
taxa_bia = 0.01

altura_p=float(input("Digite a altura: "))
taxa_p=float(input("Digite a taxa: "))

ano=0

while altura_p<altura_bia:
	altura_bia = altura_bia + taxa_bia
	altura_p = altura_p + taxa_p
	ano = ano+1
print(ano)
	

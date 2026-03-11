altura_bia = 1.69
taxa_bia = 0.01

altura = float(input("insira um numero:"))
taxa = float(input("insira um numero: "))

ano = 0

while altura < altura_bia:
	altura_bia = altura_bia + taxa_bia
	altura = altura + taxa
	ano += 1 
print(ano)
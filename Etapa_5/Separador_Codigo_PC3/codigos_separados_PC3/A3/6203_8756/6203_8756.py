altura_leao = float(input())
taxa = float(input())
altura_macaco = 1.4
taxa_macaco = 0.06
cont = 0

while altura_macaco < altura_leao:
	cont = cont + 1
	altura = altura_macaco * taxa_macaco
	if altura_macaco > altura_leao:
		altura = altura_leao * taxa
print(cont)
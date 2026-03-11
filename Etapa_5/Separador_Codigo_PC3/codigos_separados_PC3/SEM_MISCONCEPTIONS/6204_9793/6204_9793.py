altura_macaco = 1.86
taxa_macaco = 0.01
altura_coelho = float(input('num: '))
taxa_coelho = float(input('num: '))

cont = 0

while altura_coelho < altura_macaco:
	cont = cont + 1
	altura_coelho = altura_coelho + taxa_coelho
	altura_macaco = altura_macaco + taxa_macaco
	
print(cont)
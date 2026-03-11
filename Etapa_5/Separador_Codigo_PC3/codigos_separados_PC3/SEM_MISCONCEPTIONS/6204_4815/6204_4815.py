altura_macaco = 1.86
taxa_macaco = 0.01
altura_coelho = float(input())
taxa_coelho = float(input())
cont_anos = 0
while (altura_coelho <= altura_macaco):
	altura_macaco += taxa_macaco
	altura_coelho += taxa_coelho
	cont_anos += 1
print(cont_anos)
altura_macaco = 1.86
taxa_macaco = 0.01
anos = 0
altura_coelho = float(input())
taxa_coelho = float(input())

while altura_coelho <= altura_macaco:
	anos = anos + 1
	altura_coelho = altura_coelho + taxa_coelho
	altura_macaco = altura_macaco + taxa_macaco
print(anos)
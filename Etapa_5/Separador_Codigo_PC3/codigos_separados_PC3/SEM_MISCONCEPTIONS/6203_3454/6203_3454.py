altura_macaco = 1.4
taxa_macaco = 0.06

altura_leao = float(input())
taxa_leao = float(input())

anos = 0

while altura_leao > altura_macaco:
	altura_leao += taxa_leao
	altura_macaco += taxa_macaco
	anos += 1
print(anos)
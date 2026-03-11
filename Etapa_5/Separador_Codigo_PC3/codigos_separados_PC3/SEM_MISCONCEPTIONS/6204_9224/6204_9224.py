altura_macaco = 1.86
taxa_macaco = 0.01

altura_coelho = float(input("digite:"))
taxa_coelho =float(input("digite"))

anos = 0

while altura_macaco >= altura_coelho:
	altura_coelho = altura_coelho + taxa_coelho
	altura_macaco = altura_macaco + taxa_macaco
	anos += 1
	
print(anos)
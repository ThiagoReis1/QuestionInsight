altura_macaco = 1.86
taxa_macaco = 0.01
anos = 0

altura_c = float(input("Altura do coelho: "))
taxa_c = float(input("Taxa do coelho: "))

while altura_c <= altura_macaco:
	altura_macaco += taxa_macaco
	altura_c += taxa_c
	anos += 1
print(anos)
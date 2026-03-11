altura_macaco = 1.4
taxa_macaco = 0.06

altura_felino = float(input("digite a altura: "))
taxa_crescimento = float(input("digite a taxa de crescimento: "))
cont = 0

while(altura_macaco < altura_felino):
	altura_felino += taxa_crescimento
	altura_macaco += taxa_macaco
	cont = cont + 1
print(cont)

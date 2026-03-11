altura_macaco = 1.4
taxa_macaco = 0.06

alt= float(input("digite a altura"))
tc= float(input("digite a taxa de crescimento"))

cont = 0

while altura_macaco<alt:
	alt = alt + tc
	altura_macaco = altura_macaco + taxa_macaco
	cont = cont + 1
	
	
print(cont)
	

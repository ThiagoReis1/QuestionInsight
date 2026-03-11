altura_macaco = 1.4
taxa_macaco = 0.06

altura_leao = float(input("digite a altura do leao: "))
taxa_leao = float(input("digite a taxa: "))

cont = 0 

while (altura_macaco < altura_leao):
	altura_macaco = altura_macaco + taxa_macaco
	altura_leao = altura_leao + taxa_leao
	cont += 1
	
print(cont)
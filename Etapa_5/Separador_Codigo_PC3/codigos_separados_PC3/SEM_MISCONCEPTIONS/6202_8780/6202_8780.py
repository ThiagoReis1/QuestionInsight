alt_bia = 1.69
taxa_bia = 0.01
cont = 0

alt_x = float(input("Digite a altura: "))
taxa_x = float(input("Digite a taxa de crescimento: "))

while alt_bia > alt_x:
	alt_bia = alt_bia + taxa_bia
	alt_x = alt_x + taxa_x
	cont+= 1
print(cont)
h = float(input("Digite a altura: "))
tx = float(input("Digite a taxa de crescimento anual: "))

altura_bia = 1.69
taxa_bia = 0.01
t = 0

while altura_bia > h:
	altura_bia = altura_bia + taxa_bia
	h += tx
	t += 1
	
print(t)
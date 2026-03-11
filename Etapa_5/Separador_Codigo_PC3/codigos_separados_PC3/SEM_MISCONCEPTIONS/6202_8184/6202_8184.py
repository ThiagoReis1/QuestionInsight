altura_bia = 1.69
taxa_bia = 0.01
ap = float(input("altura: "))
tp = float(input("taxa: "))
cont = 0
while (altura_bia > ap):
	altura_bia = altura_bia + taxa_bia
	ap = ap + tp
	cont = cont + 1
print(cont)
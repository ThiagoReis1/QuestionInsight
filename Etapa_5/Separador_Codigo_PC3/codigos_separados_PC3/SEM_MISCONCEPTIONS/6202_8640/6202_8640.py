altura_bia = 1.69
taxa_bia = 0.01
anos = 0
rafa = float(input("digite a altura:"))
taxa = float(input("taxa de altura:"))

while (altura_bia > rafa):
	altura_bia = taxa_bia + altura_bia
	rafa += taxa
	anos += 1
print(anos)

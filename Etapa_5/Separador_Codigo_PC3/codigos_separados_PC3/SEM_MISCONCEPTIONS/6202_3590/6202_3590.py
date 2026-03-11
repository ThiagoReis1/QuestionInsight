altura_bia = 1.69
taxa_bia = 0.01

altura = float(input())
taxa = float(input())
total = 0

while(altura < altura_bia):
	altura = altura + (taxa)
	altura_bia = altura_bia + (taxa_bia)
	total += 1
	
print(total)
	
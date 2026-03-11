altura_bia = 1.69
taxa_bia = 0.01
#
altura = float(input("alt:"))
taxa = float(input("tx:"))

anos = 0

while(altura < altura_bia):
	altura_bia += taxa_bia
	altura += taxa
	anos += 1

print (anos)
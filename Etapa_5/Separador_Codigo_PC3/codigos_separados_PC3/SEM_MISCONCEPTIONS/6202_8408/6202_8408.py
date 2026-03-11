anos = 0
altura_bia = 1.69
taxa_bia = 0.01
altura_p = float(input("altura: "))
taxa_p = float(input("taxa de crescimento: "))

while (altura_bia > altura_p):
	anos = anos + 1
	altura_bia = altura_bia + taxa_bia
	altura_p = altura_p +taxa_p
	
print(anos)	
	
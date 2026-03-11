altura_cicero = 1.75
taxa_cicero = 0.01
altura = float(input("altura: "))
taxa = float(input("altura: "))
anos = 0 

while (altura < altura_cicero):
	altura_cicero = altura_cicero + taxa_cicero
	altura = altura + taxa
	anos = anos + 1
	
	
print(anos)
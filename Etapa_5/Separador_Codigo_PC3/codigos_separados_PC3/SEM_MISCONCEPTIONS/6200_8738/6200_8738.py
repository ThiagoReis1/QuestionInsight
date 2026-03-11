altura_cicero = 1.75
taxa_cicero = 0.01

feli = float(input("altura de max"))
taxa = float(input("taxa de crescimento de max: "))

anos = 0

while feli < altura_cicero:
	altura_cicero += taxa_cicero
	feli += taxa
	anos+= 1
	
print(anos)
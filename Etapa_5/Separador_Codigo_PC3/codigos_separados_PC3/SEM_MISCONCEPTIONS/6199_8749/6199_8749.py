altura_Cicero = 1.8
taxa_Cicero = 0.01

feli = float(input("altura de Cicero"))
taxa = float(input("taxa de crescimento de Cicero: "))

anos = 0

while feli < altura_Cicero:
	altura_Cicero += taxa_Cicero
	feli += taxa 
	anos+= 1
	
print(anos)
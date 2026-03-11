altura_cicero = 1.8
taxa_cicero = 0.01

altura = float(input())
taxa_crescimento = float(input())
anos = 0

while altura <= altura_cicero:
	altura_cicero = altura_cicero + taxa_cicero
	anos += 1
	altura = altura + taxa_crescimento

if altura > altura_cicero:
	
	print(anos)
	
	
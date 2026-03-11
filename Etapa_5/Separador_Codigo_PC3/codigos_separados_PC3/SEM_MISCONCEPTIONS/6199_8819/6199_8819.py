altura_cicero = 1.8
taxa_cicero = 0.01
anos = 0
altura = float(input())
taxa = float(input())

while altura <= altura_cicero:
	altura = altura + taxa
	altura_cicero = altura_cicero + taxa_cicero
	anos = anos + 1
print(anos)
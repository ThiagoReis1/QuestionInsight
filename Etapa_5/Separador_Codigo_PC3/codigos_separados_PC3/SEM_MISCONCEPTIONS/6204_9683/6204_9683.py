altura_macaco = 1.86
taxa_macaco = 0.01
anos = 0
altura = float(input("Digite sua altura:"))
taxa = float(input("Agora digite sua taxa de crescimento:"))

while altura < altura_macaco:
	altura_macaco += taxa_macaco
	altura += taxa
	anos += 1
print(anos)
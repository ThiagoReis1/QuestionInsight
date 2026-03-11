altura_macaco = 1.86
taxa_macaco = 0.01
altura = float(input(''))
taxa = float(input(''))
cont = 0
anos = 0
taxa1 = 0
while(altura<altura_macaco):
	anos = anos + 1
	altura = altura + taxa
	altura_macaco = altura_macaco + taxa_macaco
	
print(anos)
	
	
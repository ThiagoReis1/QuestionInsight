sg = input("Sequencia de DNA ")

soma = 0

while (sg != "S"):
	if(sg != "A"):
		sg = input("Sequencia de DNA ")
	else:
		soma = soma + 1
		sg = input("Sequencia de DNA ")
		
	
print(soma)

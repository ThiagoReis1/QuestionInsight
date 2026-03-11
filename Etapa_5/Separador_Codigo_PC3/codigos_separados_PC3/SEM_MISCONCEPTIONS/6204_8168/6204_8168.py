altura_macaco = 1.86
taxa_macaco = 0.01

fel=float(input(""))
txfel=float(input(""))
cont=0

while(fel<=altura_macaco and txfel>taxa_macaco):
	cont=cont+1
	fel=fel+txfel
	altura_macaco=altura_macaco+taxa_macaco
	
print(cont)


	
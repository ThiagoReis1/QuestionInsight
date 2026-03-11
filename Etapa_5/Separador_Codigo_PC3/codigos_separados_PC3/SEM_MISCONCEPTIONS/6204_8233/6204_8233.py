macaco = 1.86
taxa_macaco = 0.01
coelho=float(input("altura coelho:"))
taxa=float(input("taxa de crecimento"))
cont=0
while(coelho < macaco):
	coelho = coelho + taxa
	macaco = macaco + taxa_macaco
	cont = cont + 1
print(cont)
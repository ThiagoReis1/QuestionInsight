altura_luna = 1.65
taxa_luna = 0.02

altura=float(input("valor "))
taxa=float(input("valor "))
cont=0

while(altura < altura_luna):
	altura_luna=altura_luna +taxa_luna
	altura=altura+taxa
	cont=cont+1
print(cont)
	
	
	
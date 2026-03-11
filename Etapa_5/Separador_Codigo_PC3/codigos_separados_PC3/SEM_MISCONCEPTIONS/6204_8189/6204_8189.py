altura_macaco = 1.86
taxa_macaco = 0.01
a=float(input("altura do coelho ?: "))
c=float(input("crecimento do coelho ?: "))
cont=0

while (altura_macaco > a ):
	altura_macaco = altura_macaco + taxa_macaco
	a = a + c
	cont = cont + 1
	
print(cont)


			


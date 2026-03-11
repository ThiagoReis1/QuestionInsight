
altura_bia = 1.69
taxa_bia = 0.01
cont=0

al=float(input(""))
tx=float(input(""))

while altura_bia > al:
	altura_bia = altura_bia+taxa_bia
	al = al + tx
	cont=cont+1
	
print(cont)
	

from numpy import*

v = input("digite o pedido?; ").upper()

i = 0 
cont = 0
cont1 = 0 
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
while ( i < len(v)):
	if (v[i] == "H"):
		cont = cont + 3.85
		cont2 = cont2 + 1
	elif (v[i] == "L"):
		cont3 = cont3 + 2.95
		cont4 = cont4 + 1
	elif ( v[i] == "E"):
		cont5 = cont5 + 7.90
		cont6 = cont6 + 1	
	i = i + 1
contat = cont + cont3 + cont5
contc = round(contat, 2)
print(contc, cont2, cont4, cont6)
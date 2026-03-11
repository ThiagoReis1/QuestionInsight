p = float(input())
d = int(input())
m = input()                                        

if(d != 1,2,3,4,5,6,7):
	print("Entradas:", p, ",", d, ",", m)
	print("Dados invalidos")
	
if(m != "S" and m != "N"):
	print("Entradas:", p, ",", d, ",", m)
	print("Dados invalidos")
	
else:
	if(d == 2 or d == 3 or d==5):
		c = p - (p*0.25)
		if(m == "S"):
			c = c + 20
		print("Entradas:", p, ",", d, ",", m)
		print("Valor a pagar: R$", round(c, 2))
	else:
		if(m == "S"):
			c = p + 20
		print("Entradas:", p, ",", d, ",", m)
		print("Valor a pagar: R$", round(c, 2))

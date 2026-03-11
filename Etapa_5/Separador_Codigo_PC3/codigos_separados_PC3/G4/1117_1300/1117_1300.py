p = float(input("Digite o preço normal da boate "))
d = int(input("Digite o numero do dia: "))	
m = input("Hoje é dia de música ao vivo?")
print("Entradas:", p, ",", d, ",", m)
v = p - (p* 25/100)
if(p>=0):
	if(d >=1 and d<=7):
		if(m == "S" or m == "N"):
			if(m == "S"):
				if(d == 2 or d == 5 or d == 3):
					print("Valor a pagar: R$", round(v + 20,2))
				else:
					print("Valor a pagar: R$", round(p + 20,2))
			if(m == "N"):
				if(d == 2 or d == 5 or d == 3):
					print("Valor a pagar: R$", round(v,2))
				else:
					print("Valor a pagar: R$", round(p,2))
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")
            	
                          


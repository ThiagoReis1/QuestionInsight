C = input("classe da missao ")
V = float(input("valor a ser pago ")) 

A = "Jounin"
B = "Chunin"

if (C == "A"):
	b = V-V*22/100
	print ("Classe:", A)
	print (round (b,2))

else:
	d = V-V*15/100
	print ("Classe:", B)
	print (round(d,2))
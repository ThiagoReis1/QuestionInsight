r = input("")
q = input("")

if (r == "Campeao") and ((q == "05-vezes") or (q == "04-vezes")):
	if(q == "05-vezes"):
		print ("BRASIL")
	else:
		print("ITALIA")
elif (r == "Vice-Campeao") and ((q == "03-vezes") or (q == "04-vezes")):
	if(q == "03-vezes"):
		print ("ARGENTINA")
	else:
		print("ALEMANHA")
else:
	print("SELECAO NAO IDENTIFICADA")
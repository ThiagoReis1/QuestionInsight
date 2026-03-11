c= input("cidade de destino:").lower()
i= int(input("idade do passageiro:"))

if(c == "porto velho") or (c == "santarem") or (c == "belem") or (c == "tefe") or (c == "tabatinga"):
	if(c=="porto velho"):
		t=(500)
	elif(c=="santarem"):
		t=(370)
	elif(c=="belem"):
		t=(600)
	elif(c=="tefe"):
		t=(360)
	elif(c=="tabatinga"):
		t=(550)
	else:
		print("Entradas invalidas")

if(i < 0) and (i >150):
	print("Entradas invalidas")
elif(i > 0) and (i <= 2):
	t=(0.0)
	print("Passagem: R$", round(t,2))
elif(i >= 3) and (i <= 12):
	t=(t/2)
	print("Passagem: R$", round(t,2))
elif(i >= 65):
	t=(t - (t*30/100))
	print("Passagem: R$", round(t,2))
else:
	print("Entradas invalidas")

			
	
		
ano= int(input(":"))
pais= input(":")
pais= pais. upper()
idade=2023-ano
if pais == "B":
	im=21
	if idade > im:
		print ("sim")
		print(idade - im)
	else:
		print("nao")
		print(im % idade)
elif pais == "J":
	im=20
	if idade > im:
		print ("sim")
		print( im - idade)
	else:
		print("nao")
		print (im % idade)
else:
	print("invalido")
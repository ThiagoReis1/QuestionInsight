amina = input ()
o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079

if ((amina.lower() == "histidina") or (amina.lower() == "leucina") or (amina.lower() == "lisina")):
	if (amina.lower() == "histidina"):
		peso = ((c * 6) + (h * 10) + (n * 3) + (o * 2))
	elif (amina.lower() == "leucina"):
		peso = ((c * 6) + (h * 13) + (n * 1) + (o * 2))
	else:
		peso = ((c * 6) + (h * 15) + (n * 2) + (o * 2))
	print (round(peso, 2))

else:
	print ("Entrada:", amina)
	print ("Dado Invalido")
	


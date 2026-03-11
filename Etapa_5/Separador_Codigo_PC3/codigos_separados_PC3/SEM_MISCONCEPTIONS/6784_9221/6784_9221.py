ano= int (input ("Digite seu ano de nascimento: "))
pais= input ("Digite B para Brasil e R para reino unido: ").upper()
idademin = 2023 - ano

if (pais == "B") and (idademin >= 21):
	apta= idademin - 21
	print ("sim")
	print (apta)
elif (pais == "R") and (idademin >= 18):
	apta= idademin - 18
	print ("sim")
	print (apta)
elif (idademin < 18) and (pais == "R"):
	naoApto= 18 - idademin
	print ("nao")
	print (naoApto)
elif (idademin < 21) and (pais == "B") :
	naoApto= 21 - idademin
	print ("nao")
	print (naoApto)
else:
	print ("invalido")
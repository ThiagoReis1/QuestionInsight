c=input("digite campeao ou vice:").upper()
v=input("digite quantas vezes camepao:")

if(c=="CAMPEAO" or c=="vice-campeao"):
	if(c=="CAMPEAO") and (v=="06-vezes"):
		print("CORINTHIANS")
	elif(c=="CAMPEAO") and (v=="03-vezes"):
		print("SANTOS")
	elif(c=="vice-campeao") and (v=="01-vez"):
		print("FLAMENGO")
	elif(c=="vice-campeao") and (v=="06-vezes"):
		print("INTERNACIONAL")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO.")
  
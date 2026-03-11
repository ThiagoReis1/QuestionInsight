r=input("campeão ou vice: ")
v=input("Vezes:")
if(r=="Campeao"):
	if(v=="05-vezes"):
		time="brasil"
		print(time.upper())
	elif(v=="04-vezes"):
		time="italia"
		print(time.upper())
	else:print("SELECAO NAO IDENTIFICADA")
		
if(r=="Vice-Campeao"):
	if(v=="04-vezes"):
		time="alemanha"
		print(time.upper())
	elif(v=="03-vezes"):
		time="argentina"
		print(time.upper())
	else:
		print("SELECAO NAO IDENTIFICADA")
		



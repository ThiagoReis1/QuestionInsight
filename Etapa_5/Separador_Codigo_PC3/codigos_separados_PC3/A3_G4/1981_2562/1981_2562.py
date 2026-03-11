x= input("qualquer coisa? : ").lower()
y= input("vezes campeao? : ") 

co= "Corinthians"
sa= "Santos"
fla= "Flamengo"
colorado= "Internacional"

if(x=="campeao" or x=="vice-campeao"):
	if(x=="campeao"):
		if(y=="06-vezes"):
			print((co).upper())
		elif(y=="03-vezes"):
			print((sa).upper())
		else:
			print("TIME DE FUTEBOL NAO IDENTIFICADO")
	elif(x=="vice-campeao"):
		if(y=="01-vez"):
			print((fla).upper())
		elif(y=="06-vezes"):
			print((colocado).upper())
		else:
			print("TIME DE FUTEBOL NAO IDENTIFICADO")
	else:
		print("TIME DE FUTEBOL NAO IDENTIFICADO")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")
		
		

	
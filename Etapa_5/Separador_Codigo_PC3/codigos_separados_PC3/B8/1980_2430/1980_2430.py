estado = input("Digite o nome do Estado: ")
cidade = input("Digite o nome da Cidade: ")

if((estado == "Amazonas") or (estado == "Para")): 
	if(estado == "Amazonas"):
		if(cidade == "Manaus" or cidade == "Parintins"):
			if(cidade == "Manaus"):
				print("Coroado".upper())
			elif (cidade == "Parintins"):
				print("PALMARES".upper())
		else:
			print("Bairro nao identificado".upper())
	else:
		if( estado == "Para"):
			if((cidade =="Belem") or (cidade == "Santarem")):
				if(cidade == "Belem"):
					print ("Cidade velha".upper() )
				elif(cidade == "Santarem"):
					print("Centro".upper())
		else:
			print("Bairro nao identificado".upper())
else:
	print("Bairro nao identificado".upper())
			
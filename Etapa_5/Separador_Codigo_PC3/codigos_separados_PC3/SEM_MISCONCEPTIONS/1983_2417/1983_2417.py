continente = input("")
pais = input("")
if (continente != "Asia") and (continente != "America-do-Sul"):
	if (pais != "Jordania") and (pais != "India") and (pais != "Peru") and (pais != "Brasil"):
		mensagem = "Informacao nao identificada"
		print(mensagem.upper())
	else :
		
		
		mensagem = "As ruinas de petra"
		print(mensagem.upper())
	else :
		mensagem = "Taj Mahal"
		print(mensagem.upper())
elif (continente == "America-do-Sul"):
	if (pais == "Peru") :
		mensagem = "Machu Picchu"
		print(mensagem.upper())
	else :
		mensagem = "Cristo Redentor"
		print(mensagem.upper())
else :
	mensagem = "Informacao nao identificada"
	print(mensagem.upper())
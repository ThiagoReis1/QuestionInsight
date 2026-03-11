continente = input("Digite o continente: ")
pais = input("Digite o pais: ")


if(continente == "Asia" and pais == "Jordania"):
	maravilha = "as ruinas de petra"
elif(continente == "Asia" and pais == "India"):
	maravilha = "taj mahal"
elif(continente == "America-do-Sul" and pais == "Peru"):
	maravilha = "machu picchu"
elif(continente == "America-do-Sul" and pais == "Brasil"):
	maravilha = "cristo redentor"
else:
	maravilha = "informacao nao identificada"
	
print(maravilha.upper())
	
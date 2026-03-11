#Estilo de genero:
gen = input("Estilo de genero musical: ")
sub = input("Subgenero musical: ")

if(gen=="Misturado"):
	if(sub == "Samba-jazz"):
		print("saxofone".lower())
	else:
		print("baixo".lower())
		if(gen=="Misturado"):
			if(sub=="Rock"):
				print("guitarra".lower())
			else:
				print("bateria".lower())
else:
	print("instrumento nao identificado".lower())

	
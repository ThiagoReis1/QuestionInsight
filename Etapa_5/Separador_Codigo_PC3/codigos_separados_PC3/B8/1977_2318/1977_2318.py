genero = input("Digite o nome do genero: ")
subgenero = input("Digite o nome do subgenero: ")

if (genero != "Investigativa" and genero != "Dramatica") or (subgenero != "Suspense" and subgenero != "Drama" and subgenero != "Com ficçao" and subgenero != "Aventura"):
	print("SERIE NAO IDENTIFICADA")
else:
	if genero == "Investigativa" and subgenero == "Suspense":
		X = "dexter"
		print(X.upper())
	elif genero == "Investigativa" and subgenero == "Drama":
		X = "narcos"
		print(X.upper())
	elif genero == "Dramatica" and subgenero == "Com ficcao":
		X = "lost"
		print(X.upper())
	elif genero == "Dramatica" and subgenero == "Aventura":
		X = "sherlock"
		print(X.upper())
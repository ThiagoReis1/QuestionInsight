C = input("O gênero de série: ")
P = input("O subgênero da série: ")

if C == "INVESTIGATIVA" and P == "SUSPENSE":
	R= "DEXTER"
	print(R.upper())
elif C == "INVESTIGATIVA" and P == "DRAMA":
	R= "NARCOS"
	print(R.upper())
elif C == "DRAMATICA" and P == "COM FICCAO":
	R="LOST"
	print(R.upper())
elif C == "DRAMATICA" and P == "AVENTURA":
	R="SHERLOCK"
	print(R.upper())
else:
	print("SERIE NAO IDENTIFICADA")
	
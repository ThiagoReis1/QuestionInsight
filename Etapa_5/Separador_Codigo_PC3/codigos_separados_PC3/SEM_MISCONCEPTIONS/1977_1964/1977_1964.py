G = input("Digite o Genero da serie: ").upper()
S = input("Digite o sub genero: ").upper()

if(G=="INVESTIGATIVA" and S=="SUSPENSE"):
	serie ="dexter"
	print(serie.upper())
elif(G=="INVESTIGATIVA" and S=="DRAMA"):
	serie = "narcos"
	print(serie.upper())
elif(G=="DRAMATICA" and S=="COM FICÇAO"):
	serie = "lost"
	print(serie.upper())
elif(G=="DRAMATICA" and S=="AVENTURA"):
	serie = "SHERLOCK"
	print(serie.upper())
else:
	print("SERIE NAO IDENTIFICADA")
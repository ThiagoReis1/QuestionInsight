regiao=input("regiao: ")
estado=input("estado: ")
regiao=regiao.upper()
estado=estado.upper()
if regiao=="NORTE" and estado=="AMAZONAS":
	print("Universidade Federal do Amazonas".upper())
elif regiao=="NORTE" and estado=="RORAIMA":
	print("Universidade federal de Roraima")
elif regiao=="SUL" and estado=="PARANA":
	print("Universidade Federal do Parana".upper())
elif regiao=="SUL" and estado=="SANTA CATARINA":
	print("Universidade Federal de Santa Catarina".upper())
else:
	print("UNIVERSIDADE NAO IDENTIFICADA".upper())
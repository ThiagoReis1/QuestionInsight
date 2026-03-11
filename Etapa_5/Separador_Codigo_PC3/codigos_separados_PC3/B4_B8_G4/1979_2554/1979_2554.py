C = input("O resultado da selecao na competicao: ")
N = input("Qnts vezes a selecao alcancou o resultado: ")
if(not(C == "Campeao" or C == "Vice-Campeao")):
	print("SELECAO NAO IDENTIFICADA")
else:
	if(not(N == "03-vezes" or N == "04-vezes" or N == "05-vezes")):
		print("SELECAO NAO IDENTIFICADA")
	else:
		if(C == "Campeao"):
			if(N == "05-vezes"):
				print("brasil".upper())
			else:
				if(N == "04-vezes"):
					print("italia".upper())
		else:
			if(C == "Vice-Campeao"):
				if(N == "04-vezes"):
					print("alemanha".upper())
				else:
					if(N == "03-vezes"):
						print("argentina".upper())

		

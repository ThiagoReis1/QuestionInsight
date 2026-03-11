x = input("Digite o nome do aminoacido: ")
if(x == "Aspartato".lower()):
	print(round((4 * 12.011) + (6 * 1.0079) + (14.0067) + (4 *15.9994),2))
elif(x == "Fenilalanina".lower()):
	print(round((9 * 12.011) + (11 * 1.0079) + (2 * 15.9994) + (32.066),2))
elif(x == "Tirosina".lower()):
	print(round((9 * 12.011 ) + (11 * 1.0079) + (14.0067) + (3 * 15.9994),2))
else:
	print("Entrada: ",x)
	print("Dado Invalido")
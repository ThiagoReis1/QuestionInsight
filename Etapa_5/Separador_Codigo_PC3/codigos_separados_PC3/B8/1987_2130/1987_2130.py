aminoacido = input("digite aminoacido: ")

O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794

Alanina = C * 3 + H * 7 + N * 1 + O * 2
Valina = C * 5 + H * 11 + N * 1 + O * 2
Tirosina = C * 9 + H * 11 + N * 1 + O * 3

if	(aminoacido.upper() != "ALANINA") and (aminoacido.upper() != "VALINA") and (aminoacido.upper() != "TIROSINA"):
	print("Entrada: ", aminoacido.upper())
	print("Dado Invalido")
else:
	if	(aminoacido.upper() == "ALANINA"):
		print(round(Alanina, 2))
	elif	(aminoacido.upper() == "VALINA"):
		print(round(Valina, 2))
		
	elif	(aminoacido.upper() == "TIROSINA"):
		print(round(Tirosina, 2))
	

 
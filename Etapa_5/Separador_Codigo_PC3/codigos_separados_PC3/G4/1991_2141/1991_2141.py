aminoacido = input("aminoacido: ")

O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794

if(aminoacido.upper() == "GLICINA"):
	x = (C * 2) + (H * 5) + N + (O * 2)
	print(round(x, 2))
elif(aminoacido.upper() == "PROLINA"):
	x = (C * 5) + (H * 10) + N + (O * 2)
	print(round(x, 2))
elif(aminoacido.upper() == "SERINA"):
	x = (C * 3) + (H * 7) + N + (O * 3)
	print(round(x, 2))
else:
	print("Entrada:", aminoacido)
	print("Dado Invalido")
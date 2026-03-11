aminoacido = input("Aspartato, Cisteina ou Metionina: ").lower()

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if(aminoacido == "aspartato"):
	x = (C * 4) + (H * 6) + N + (O * 4)
	print(round(x, 2))
elif(aminoacido == "cisteina"):
	x = (C * 3) + (H * 7) + N + (O * 2) + S
	print(round(x, 2))
elif(aminoacido == "metionina"):
	x = (C * 5) + (H * 11) + N + (O * 2) + S
	print(round(x, 2))
else:
	print("Entrada:", aminoacido)
	print("Dado Invalido")
aminoacido = input("nome do aminoacido: ").upper()

O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794

if(aminoacido == "GLUTAMINA"):
	pm = (C * 5) + (H * 8) + N  + (O * 4)
else :
	pm = (C * 4) + (H * 9) + N + (O * 3)
	
print(round(pm,2))

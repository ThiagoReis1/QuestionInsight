comida = input()

if comida.upper() == "T":
	tapiocas = int(input())
	acai = int(input())
	
	total = (tapiocas * 3.5) + (acai * 13)
	print(round(total,2))
else:
	salgado = int(input())
	acai = int(input())
	
	total = (salgado * 5) + (acai * 13)
	print(round(total,2))
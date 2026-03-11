TouS = (input("Escreva se vai querer tapioca usando T ou salgado usando S: "))
tous = int(input("Quantidade de tapiocas ou salgados: "))
A = int(input("Quantidade de acai: "))

if TouS == "T":
	total = (tous * 5.50) + (A * 10)
	print(total)
	
if TouS == "S":
	total = (tous * 4) + (A * 10)
	print(total)
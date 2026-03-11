p = int(input("peso: "))
d = int(input("distancia: "))
c = int(input("codigo: "))
valor = ((p*25) + (d*0.10)) * (1.0+(c/100))
if(c == 1):
	c = 17
	valor = ((p*25) + (d*0.10)) * (1.0+(c/100))
	print(round(valor,2))
if(c == 2):
	c = 17.5
	valor = ((p*25) + (d*0.10)) * (1.0+(c/100))
	print(round(valor,2))
if(c == 3):
	c = 18
	valor = ((p*25) + (d*0.10)) * (1.0+(c/100))
	print(round(valor,2))
if(c == 4):
	c = 20
	valor = ((p*25) + (d*0.10)) * (1.0+(c/100))
	print(round(valor,2))
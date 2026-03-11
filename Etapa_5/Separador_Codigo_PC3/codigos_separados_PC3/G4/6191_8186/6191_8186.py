face = input("Diga a face: ").upper()

cont = 0
soma = 0

while (face != "S"):
	if (face == "CARA"):
		soma = soma + 1
		cont = cont + 1
		
	face = input("Diga a frase: ").upper()
	
print(cont)
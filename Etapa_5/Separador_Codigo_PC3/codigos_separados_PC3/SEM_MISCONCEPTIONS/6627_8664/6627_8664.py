# faça seu código aqui!

frase = input("Frase: ")
frase = frase.upper()

cont_e = 0
i = 0 
tam = len(frase)

while i < tam:
	if frase[i] == "D":
		cont_e += 1
		
	i += 1

print(cont_e)
	
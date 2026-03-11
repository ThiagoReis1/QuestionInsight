aminoacido = input("Digite nome do aminoacido: ").upper()

soma_glutamina = (5*12.011 + 8*1.00794 + 1*14.0067 + 4*15.9994)
soma_serina = (3*12.011 + 7*1.00794 + 1*14.0067 + 3*15.9994)
soma_treonina = (4*12.011 + 9*1.00794 + 1*14.0067 + 3*15.9994)

if aminoacido == "glutamina".upper():
	print(round(soma_glutamina, 2))
elif aminoacido == "serina".upper():
	print(round(soma_serina, 2))
elif aminoacido == "treonina".upper():
	print(round(soma_treonina, 2))
else:
	print("Entrada:", aminoacido)
	print("Dado Invalido")
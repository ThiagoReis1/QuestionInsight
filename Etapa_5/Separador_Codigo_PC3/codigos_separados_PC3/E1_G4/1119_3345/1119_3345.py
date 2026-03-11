x = str(input("Casa: "))
X = x.lower()
if (X == "baratheon") or (X == "targaryen") or (X == "tyrell") or (X == "stark") or (X == "lannister") or (X == "greyjoy") or (X == "tully") or (X == "arryn") or (X == "martell"):
	if (X == "baratheon"):
		m = "Nossa e a furia"
	elif (X == "targaryen"):
		m = "Fogo e sangue"
	elif (X == "tyrell"):
		m = "Crescendo fortes"
	elif (X == "stark"):
		m = "O inverno esta chegando"
	elif (X == "lannister"):
		m = "Oucam-me rugir"
	elif (X == "greyjoy"):
		m = "Nos nao semeamos"
	elif (X == "tully"):
		m = "Familia, dever, honra"
	elif (X == "arryn"):
		m = "Tao alto como a honra"
	else:
		m = "Insubmissos, nao curvados, nao quebrados"
	print(m)
else:
	print("Entrada ", x, " invalida")
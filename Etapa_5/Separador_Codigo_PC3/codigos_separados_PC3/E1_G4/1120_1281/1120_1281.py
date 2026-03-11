c=input("Casa")
if (c=="Baratheon" or c=="Targaryen" or c=="Tyrell" or c=="Stark" or c=="Lannister" or c=="Greyjoy" or c=="Tully" or c=="Arryn" or c=="Martell"):
	if c=="Baratheon":
		r="Ponta Tempestade"
	elif c=="Targaryen":
		r="Ilha do Dragao"
	elif c=="Tyrell":
		r="Campina"
	elif c=="Stark":
		r="Winterfell"
	elif c=="Lannister":
		r="Rochedo Casterly"
	elif c=="Greyjoy":
		r="Pyke"
	elif c=="Tully":
		r="Correrio"
	elif c=="Arryn":
		r="Ninho da Aguia"
	else:
		r="Dorne"
	print(r)	
else:
	print("Entrada", c, "invalida")
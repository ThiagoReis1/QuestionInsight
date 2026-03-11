nome_de_aminoacido = input("nome de aminoacido:")

o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079

glicina = c*2 + h*5 + n + o*2
prolina = c*5 + h*10 + n + o*2
serina = c*3 + h*7 + n + o*3

if	(nome_de_aminoacido.upper() == "glicina".upper()):
	print(round(glicina, 2))
	if(nome_de_aminoacido.upper() == "prolina".upper()):
		print(round(prolina.upper(), 2))
	elif(nome_de_aminoacido.upper() == "serina".upper()):
		print(round(serina.upper(), 2))
else:
	print()
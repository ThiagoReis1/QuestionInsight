aminoacido = input("Digite o nome do aminoacido: ").lower()
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.0079

if (aminoacido == "aspartato" or aminoacido == "fenilalanina" or aminoacido == "tirosina"):
	if (aminoacido == "aspartato"):
		calculo = c*4+h*6+n+o*4
	elif (aminoacido == "fenilalanina"):
		calculo = c*9+h*11+o*2+s
	elif (aminoacido == "tirosina"):
		calculo = c*9+h*11+n+o*3
	print(round(calculo, 2))
else:
	print("Entrada: ", aminoacido)
	print("Dado Invalido")

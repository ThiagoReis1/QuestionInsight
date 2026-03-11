#Inserindo o tipo de aminoacido
m = input("Insira o nome do aminoacido: ").lower()

#Pesos moleculares de um atomo
#Oxigenio
o = 15.9994
#Carbono
c = 12.011
#Nitrogenio
n = 14.0067
#Enxofre
e = 32.066
#Hidrogenio
h = 1.0079

#Validacao de entradas
if (m != "aspartato") and (m != "fenilalanina") and (m != "tirosina"):
	print("Entrada:", m)
	print("Dado Invalido")
elif (m == "aspartato"):
	peso = (4 * c) + (6 * h) + n + (4 * o)
	print(round(peso, 2))
elif (m == "fenilalanina"):
	peso = (9 * c) + (11 * h) + (2 * o) + e
	print(round(peso, 2))
elif (m == "tirosina"):
	peso = (9 * c) + (11 * h) + n + (3 * o)
	print(round(peso, 2))





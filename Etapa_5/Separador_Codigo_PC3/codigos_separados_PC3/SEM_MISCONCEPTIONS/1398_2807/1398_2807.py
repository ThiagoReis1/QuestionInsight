tempo = int(input(""))

inicial = 200
minuto = 100*inicial

if(tempo <= 200):
	piloto = 5000
	custo = piloto + minuto
else:
	piloto = 8000
	resto = tempo - inicial
	minuto1 = (90*resto)
	custo = piloto + minuto + minuto1
	
print(float(round(custo, 2)))
escala = input("unidade de medida de distancia: ")
c = float(input("velocidade: "))

if escala == "M" :
	velocidade = 3.6*c

else:
	velocidade = (1/3.6)*c
	
print(round(velocidade,2))
from numpy import*

notas = array(eval(input("notas: ")))
pesos= [2,1,5]
i = 0
numerador = 0
denominador = 0

while i <size(notas):
	numerador = numerador + notas[i] * pesos[i]
	i = i + 1
	denominador = sum(pesos)
media = numerador/denominador
print(round(media, 2))
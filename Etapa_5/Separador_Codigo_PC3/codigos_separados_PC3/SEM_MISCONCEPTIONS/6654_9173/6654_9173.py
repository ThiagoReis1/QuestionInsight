from numpy import *
notas = array(eval(input("insira as notas: ")))
pesos = array([1,3,2,5])
denominador = sum(pesos)
numerador = 0
i = 0
while i < size(pesos):
	numerador += notas[i] * pesos[i]
	i += 1
media_ponderada = numerador / denominador
print(round(media_ponderada, 2))
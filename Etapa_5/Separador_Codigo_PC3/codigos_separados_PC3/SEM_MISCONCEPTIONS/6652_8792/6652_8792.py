from numpy import*
notas = array(eval(input('')))
pesos = [2,2,6,1]
i = 0
numerador = 0
denominador = 0

while (i < size(notas)):
	numerador = numerador + notas[i] * pesos[0]
	denominador = denominador + pesos[0:-1]
	i += 1

coeficiente = numerador/denominador
print(round(coeficiente, 2))
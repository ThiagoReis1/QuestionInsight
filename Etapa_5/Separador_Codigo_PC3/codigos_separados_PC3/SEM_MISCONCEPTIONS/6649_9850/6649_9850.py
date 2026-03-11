from numpy import*

notas = array(eval(input("Insira as notas: ")))
pesos = [3, 2, 4, 1, 3]

i = 0
numerador = 0
denominador = 0

while i < size(notas):
	numerador = numerador + notas[i] * pesos[i]
	denominador = denominador + pesos[i]
	i = i + 1 
coeficiente = numerador / denominador
print(round(coeficiente, 2))
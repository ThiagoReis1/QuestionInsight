from numpy import *
notas = array(eval(input("Informe as notas: ")))
i = 0# Variavel contadora
cred = i + 1
numerador = 0 # Acumula produto notas * creditos
denominador = 0 # Acumula os creditos
while (i < size(notas)):
	numerador = numerador + notas[i] * cred
	denominador = denominador + cred
	cred = cred + 1
	i = i + 1
coeficiente = numerador / denominador
print(round(coeficiente, 2))
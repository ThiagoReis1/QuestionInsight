from math import *
x = float(input("Numero real: "))
k = int(input("Qtd de termos: "))
i = 1 #contadora
t = 1 #crescimento
eq = 0 #acumaldora
sinal = 1 #sinal
while i <= k:
	eq += sinal * ((x ** t) /(t))
	t += 2
	i += 1
	sinal = sinal * -1
print(round(eq,6))
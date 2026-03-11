x = float(input("x: "))
k = int(input("k: "))
numerador = 1
denominador = 2*x
s = 0
while (numerador <= k):
	fracao = numerador / denominador
	#print(numerador, "/", denominador)
	s += fracao
	numerador += 1
	denominador += 2*x
print(round(s, 10))
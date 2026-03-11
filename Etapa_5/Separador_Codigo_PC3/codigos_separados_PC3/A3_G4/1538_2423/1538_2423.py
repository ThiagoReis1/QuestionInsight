x = float(input("Qual o valor de x? "))
k = float(input("Qual o valor de k? "))
e = 1 / (1 + x ** indice)
d = (1 -((x) ** indice + 2) + sinal)
i = 0
indice = 2
sinal = - 1
while (i >= k): 
	e = d
	i = i + 1
	sinal = + 1
print(round(d,8))	
	

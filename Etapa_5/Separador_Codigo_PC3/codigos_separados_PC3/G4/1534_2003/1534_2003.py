from math import*

x = float(input("Insira um número real: "))
k = int(input("Insira um número inteiro: "))

i = 0 
serie = 0

while i < k:
	w = (2*i+1)
	serie = serie + (x**w)/w
	i = i+1
	
print(round(serie, 7))
	
from math import *
ang = eval(input("angulo: "))
termos = int(input(": "))
i = 1
serie = 0
while(i <= termos):
	serie = serie + (-1) ** (i+1)((ang**(2*i-1))/(factorial(2*i)))
	i = i + 1 
	
print(round(serie, 10))
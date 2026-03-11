from math import *
x = eval(input("Angulo: "))
k = int(input("Quantide de temos: "))

soma = 0
t = 0 
sinal = 1
while(k>t):
	soma = soma + ((sinal)*(x**t))/(factorial(2*t))
	t = t + 1
	sinal = -sinal										  
print(round(soma , 6))
								
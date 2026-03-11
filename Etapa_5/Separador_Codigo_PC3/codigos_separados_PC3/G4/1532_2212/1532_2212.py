from math import *
x = float(input("Qual o numero real? "))
k = int(input("Qual a quantidade de termos? "))
#variavel acumuladora
f = 0
#contador
t = 0
while(k>t):
	
	f = ((x**(2*t+1))/factorial(2*t+1))+f
	t = t+1
	

print(round(f,9))
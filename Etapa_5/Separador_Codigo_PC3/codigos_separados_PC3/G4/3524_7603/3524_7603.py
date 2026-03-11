from math import *

x = float(input("numero real: "))
k = int(input("qtd de termos da serie: "))

s = 0
i = 0 #expoente e valor do fatorial
soma = 0 #soma total

#i = 4 k = 4
# nao pode ser i para nao pular termo na equacao
while s< k:
	cos = ((x**i) / factorial (i))
	#i = i + 2
	soma = soma + cos
	i = i + 2
	s = s + 1
	
	
print(round(soma, 8))
	

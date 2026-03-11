from numpy import *

code = array(eval(input("Escreva a sequencia numerica: ")))
contador = zeros(size(code), dtype = int)

for i in range(size(code)):
	contador[i] += (code[i])**2 
			
print(contador)


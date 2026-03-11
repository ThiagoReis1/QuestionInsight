from numpy import *

senha = input("Insira uma senha de 0 a 9 inteiros: ")

senha_alt = zeros(size(senha), dtype=int)

for i in range(size(senha)):
	if senha [i] == 0:
		senha_alt [i] = 9
	else:
		senha_alt [i] = senha [i] -1
		
		
		
print(senha_alt)



